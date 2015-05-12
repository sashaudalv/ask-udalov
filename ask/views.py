# coding=utf-8
from django.db import IntegrityError
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404, JsonResponse
from django.template.defaulttags import register
from models import CustomUser, Question, Answer, AnswerLike, QuestionLike, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from forms import LoginForm, RegisterForm, MainSettingsForm, PswSettingsForm, AvatarSettingsForm, InputAnswerForm, AskQuestionForm
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='times')
def times(number):
    return range(1, number + 1)


def index(request, tag=None):

    sortBy = request.GET.get('sort')

    questions = None

    if not sortBy:
        sortBy = 'top'

    if tag:
        try:
            t = Tag.objects.get(name=tag)
        except Tag.DoesNotExist:
            raise Http404
        questions = Question.objects.filter(tags__id=t.id)

    if not questions:
        questions = Question.objects.all()

    if sortBy == 'top':
        questions = questions.order_by('-rating')
        questions = questions[:20]
    elif sortBy == 'new':
        questions = questions.order_by('-created')
        questions = questions[0:20]
    else:
        questions = questions.order_by('created')

    page = request.GET.get('page')

    questions, page_numbers, showFirst, showLast = makePaginatorElements(questions, page, 20)

    user = getAuthenticatedUser(request)

    context = {'User' : user,'Questions' : questions, 'page_numbers' : page_numbers, 'showFirst' : showFirst, 'showLast' : showLast, 'sortBy' : sortBy, 'tag' : tag}

    return render(request, 'index.html', context)


def question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404

    user = getAuthenticatedUser(request)

    answ = None

    if user:
        if request.method == 'POST':
            form = InputAnswerForm(request.POST)
            if form.is_valid():
                answ = Answer.objects.create(user_ptr=user, question=question, text=form.cleaned_data.get('answer'))
                answ.save()

    answers = Answer.objects.filter(question=question.id).order_by('-isCorrect', '-rating', 'created')

    if answ:
        page = getPaginatorPageByElement(answers, answ, 10)
        return HttpResponseRedirect('/question/' + str(question.id) + '/?page=' + str(page) + '#answer' + str(answ.id))

    page = request.GET.get('page')

    answers, page_numbers, showFirst, showLast = makePaginatorElements(answers, page, 10)

    context = {'User' : user,'Question' : question, 'Answers' : answers, 'page_numbers' : page_numbers, 'showFirst' : showFirst, 'showLast' : showLast}

    return render(request, 'question.html', context)


@login_required(login_url='/login/')
def ask(request):
    user = getAuthenticatedUser(request)

    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            question = Question.objects.create(user_ptr=user, title=form.cleaned_data.get('title'), text=form.cleaned_data.get('text'))
            tags = form.cleaned_data.get('tags').split(',')
            for tag in tags:
                if ' ' in tag:
                    tag = tag.replace(' ', '_')
                try:
                    t = Tag.objects.get(name=tag)
                except Tag.DoesNotExist:
                    t = Tag.objects.create(name=tag)
                    t.save()

                question.tags.add(t)

            question.save()
            return HttpResponseRedirect('/question/' + str(question.id))
    else:
        form = AskQuestionForm()

    context = {'User':user, 'form':form}
    return render(request, 'ask.html', context)


def login(request):
    redirect_to = request.GET.get('next', '/')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.loginUser(request):
            return HttpResponseRedirect(redirect_to)
    else:
        form = LoginForm()

    user = getAuthenticatedUser(request)
    context = {'User':user, 'form':form, 'redirect_to':redirect_to}
    return render(request, 'login.html', context)


def logout(request):
    redirect_to = request.GET.get('next', '/')
    auth.logout(request)
    return HttpResponseRedirect(redirect_to)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.saveUser():
            return HttpResponseRedirect('/login/')
    else:
        form = RegisterForm()

    user = getAuthenticatedUser(request)
    context = {'User':user, 'form':form}
    return render(request, 'register.html', context)


def user_page(request, user_id):
    try:
        user = CustomUser.objects.get(user_ptr_id=user_id)
    except CustomUser.DoesNotExist:
        raise Http404

    member_for = timezone.now() - user.date_joined
    member_for = member_for.total_seconds() // 3600

    User = getAuthenticatedUser(request)
    context = {'User':User,'user':user, 'member_for':member_for}
    return render(request, 'user.html', context)


@login_required(login_url='/login/')
def settings(request):
    User = getAuthenticatedUser(request)

    if request.method == 'POST':
        if 'login' in request.POST:
            mainForm = MainSettingsForm(request.POST)

            if mainForm.is_valid_(User):
                User.username = mainForm.cleaned_data.get('login')
                User.email = mainForm.cleaned_data.get('email')
                User.first_name = mainForm.cleaned_data.get('nickName')
                User.save()

            login = request.POST.get('login')
            email = request.POST.get('email')
            nickName = request.POST.get('nickName')
        else:
            login = User.username
            email = User.email
            nickName = User.first_name
            mainForm = MainSettingsForm()

        if 'password1' in request.POST:
            pswForm = PswSettingsForm(request.POST)
            if pswForm.is_valid_():
                User.set_password(pswForm.cleaned_data.get('password1'))
                User.save()
        else:
            pswForm = PswSettingsForm()

        if 'avatar' in request.FILES:
            avatarForm = AvatarSettingsForm(request.POST, request.FILES)
            if avatarForm.is_valid():
                User.avatar = avatarForm.cleaned_data.get('avatar')
                User.save()
        else:
            avatarForm = AvatarSettingsForm()

    else:
        login = User.username
        email = User.email
        nickName = User.first_name
        mainForm = MainSettingsForm()
        pswForm = PswSettingsForm()
        avatarForm = AvatarSettingsForm()

    context = {'User':User, 'mainForm':mainForm, 'pswForm':pswForm, 'avatarForm':avatarForm, 'login':login, 'email':email, 'nickName':nickName}
    return render(request, 'settings.html', context)

def getPaginatorPageByElement(objects, element, objects_per_page):
    paginator = Paginator(objects, objects_per_page)

    page_number = None

    for page in range(1,paginator.num_pages + 1):
        if element in paginator.page(page):
            page_number = page

    return page_number


def makePaginatorElements(objects, page, objects_per_page):
    paginator = Paginator(objects, objects_per_page)

    try:
        page_objects = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_objects = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_objects = paginator.page(paginator.num_pages)

    showFirst = False
    showLast = False

    if int(page_objects.number) > 5:
        showFirst = True

    if int(page_objects.number) < page_objects.paginator.num_pages - 4:
        showLast = True


    if showFirst and showLast:
        page_numbers = range(page_objects.number - 3, page_objects.number + 4)
    elif not showFirst:
        page_numbers = range(1, min(page_objects.paginator.num_pages + 1, 7))
    else:
        page_numbers = range(max(page_objects.paginator.num_pages - 6, 1), page_objects.paginator.num_pages + 1)

    if len(page_numbers) == page_objects.paginator.num_pages:
        showFirst = False
        showLast = False

    return page_objects, page_numbers, showFirst, showLast

def getAuthenticatedUser(request):
    if request.user.is_authenticated():
        user = CustomUser.objects.get(user_ptr_id=request.user.id)
    else:
        user = None
    return  user


def like(request):
    if request.method == 'POST':
        response_data = {}

        user = getAuthenticatedUser(request)

        object_id = int(request.POST.get('object_id',''))
        like_type = int(request.POST.get('like_type',''))
        object_type = request.POST.get('object_type','')

        if user:
            new_rating = None
            error = None

            if object_type == 'answer':
                answ = Answer.objects.get(id=object_id)

                if user != answ.user_ptr:
                    try:
                        like = AnswerLike.objects.create(user_ptr=user, likeType=like_type, answer_id=object_id)
                        like.save()
                        var = like_type
                    except IntegrityError:
                        like = AnswerLike.objects.filter(answer_id=object_id).get(user_ptr=user)
                        var = setRatingVar(like_type, int(like.likeType))
                        like.likeType = like_type
                        like.save()

                    answ.rating = str(var + answ.rating)
                    answ.save()
                    new_rating = answ.rating
                    result = 'Create like successful!'
                else:
                    result = 'Like wasn\'t created!'
                    error = 'It is your answer!'

            elif object_type == 'question':
                quest = Question.objects.get(id=object_id)

                if user != quest.user_ptr:
                    try:
                        like = QuestionLike.objects.create(user_ptr=user, likeType=like_type, question_id=object_id)
                        like.save()
                        var = like_type
                    except IntegrityError:
                        like = QuestionLike.objects.filter(question_id=object_id).get(user_ptr=user)
                        var = setRatingVar(like_type, int(like.likeType))
                        like.likeType = like_type
                        like.save()

                    quest.rating = str(var + quest.rating)
                    quest.save()
                    new_rating = quest.rating
                    result = 'Create like successful!'
                else:
                    result = 'Like wasn\'t created!'
                    error = 'It is your question!'

            else:
                result = 'Like wasn\'t created!'
                error = 'Object not found!'

            response_data['result'] = result
            if new_rating:
                response_data['new_rating'] = new_rating
            if error:
                response_data['error'] = error

        else:
            response_data['result'] = 'Like wasn\'t created!'
            response_data['error'] = 'User is not authenticated!'

        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "No POST data!"})

def setRatingVar(like_type, last_type):
    if last_type == -1:
        if like_type == -1:
            var = 0
        else:
            var = like_type + 1
    elif last_type == 1:
        if like_type == 1:
            var = 0
        else:
            var = like_type - 1
    else:
        var = like_type
    return var


def set_correct(request):
    if request.method == 'POST':
        response_data = {}

        user = getAuthenticatedUser(request)

        answer_id = int(request.POST.get('answer_id',''))

        if user:
            answ = Answer.objects.get(id=answer_id)

            if user == answ.question.user_ptr:
                answ.isCorrect =  not answ.isCorrect
                answ.save()
                result = 'Set correct successful!'
            else:
                result = 'Set correct wasn\'t checked!'
                response_data['error'] = 'This question isn\'t your!'

            response_data['result'] = result
            response_data['new_state'] = answ.isCorrect
        else:
            response_data['result'] = 'Set correct wasn\'t checked!'
            response_data['error'] = 'User is not authenticated!'

        return JsonResponse(response_data)
    else:
        return JsonResponse({"error": "No POST data!"})
