from django.conf.urls import patterns, include, url
from django.contrib import admin
from ask.views import index, ask, login, signup, register, question

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_udalov.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', index, name='home'),
    url(r'^question/$', question, name='question'),
    url(r'^ask/$', ask, name='ask'),
    url(r'^login/$', login, name='login'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^register/$', register, name='register'),

)
