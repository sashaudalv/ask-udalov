from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index, ask, login, logout, register, question, user_page, settings, like, set_correct

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_udalov.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='home'),
    url(r'^questions/tagged/(?P<tag>\w+)/$', index, name='tagged-questions'),
    url(r'^question/(?P<question_id>\d+)/$', question, name='question'),
    url(r'^add/$', ask, name='add-question'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^signup/$', register, name='signup'),
    url(r'^settings/$', settings, name='settings'),
    url(r'^user/(?P<user_id>\d+)/$', user_page, name='user_page'),
    url(r'^like/$', like, name='like'),
    url(r'^correct/$', set_correct, name='correct'),

)
