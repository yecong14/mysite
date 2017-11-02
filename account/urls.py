from . import views
from django.conf.urls import url
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
        #url(r'^login/$',auth_views.login,name='user_login'),
		url(r'^login/$',auth_views.login,{'template_name':'account/login.html'},name='user_login'),
		url(r'^logout/$',auth_views.logout,{'template_name':'account/logout.html'},name='user_logout'),
		url(r'^register/$',views.register,name='user_register'),
                url(r'^password-change/$',auth_views.password_change,
                    {'post_change_redirect':'/account/password-change-done',
                    'template_name':'account/password_change.html'},
                    name='password_change'),
		url(r'^password-change-done/$',auth_views.password_change_done,
                    {'template_name':'account/password_change_done.html'},
                    name='password_change_done'),
    ]

