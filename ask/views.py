from django.shortcuts import render
from django.http import Http404
from django.template.defaulttags import register
from models import User, Question, Answer, AnswerLike, QuestionLike, Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

u = User.objects.get(id=1) #TODO make user identification

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter(name='times')
def times(number):
    return range(1, number + 1)


def index(request):
    sortBy = request.GET.get('sort')
    tag = request.GET.get('tag')

    if not tag and not sortBy:
        sortBy = 'top'

    if sortBy:
        if sortBy == 'top':
            q = Question.objects.all().order_by('-rating')
            q = q[:20]
        elif sortBy == 'new':
            q = Question.objects.all().order_by('-created')
            q = q[0:20:-1]
        else:
            q = Question.objects.all()

    else:
        t = Tag.objects.get(name=tag)
        q = t.questions.all()


    paginator = Paginator(q, 20) # Show 20 questions per page

    page = request.GET.get('page')

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions = paginator.page(paginator.num_pages)


    showFirst = False
    showLast = False

    if int(questions.number) > 4:
        showFirst = True

    if int(questions.number) < questions.paginator.num_pages - 4:
        showLast = True


    if showFirst and showLast:
        page_numbers = range(questions.number - 3, questions.number + 4)
    elif not showFirst:
        page_numbers = range(1, min(questions.paginator.num_pages + 1, 7))
    else:
        page_numbers = range(max(questions.paginator.num_pages - 6, 1), questions.paginator.num_pages + 1)

    if len(page_numbers) == questions.paginator.num_pages:
        showFirst = False
        showLast = False

    context = {'User' : u,'Questions' : questions, 'page_numbers' : page_numbers, 'showFirst' : showFirst, 'showLast' : showLast, 'sortBy' : sortBy, 'tag' : tag}

    return render(request, 'index.html', context)


def question(request, question_id):
    try:
        q = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        raise Http404

    a = Answer.objects.filter(question=q.id).order_by('created')

    paginator = Paginator(a, 10) # Show 10 answers per page

    t = Tag.objects.filter(questions__id=q.id)

    page = request.GET.get('page')

    try:
        answers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        answers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        answers = paginator.page(paginator.num_pages)


    showFirst = False
    showLast = False

    if int(answers.number) > 4:
        showFirst = True

    if int(answers.number) < answers.paginator.num_pages - 4:
        showLast = True


    if showFirst and showLast:
        page_numbers = range(answers.number - 4, answers.number + 5)
    elif not showFirst:
        page_numbers = range(1, min(answers.paginator.num_pages + 1, 7))
    else:
        page_numbers = range(max(answers.paginator.num_pages - 6, 1), answers.paginator.num_pages + 1)

    if len(page_numbers) == answers.paginator.num_pages:
        showFirst = False
        showLast = False

    context = {'User' : u,'Question' : q, 'Answers' : answers, 'Tags' : t, 'page_numbers' : page_numbers, 'showFirst' : showFirst, 'showLast' : showLast}

    return render(request, 'question.html', context)


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')