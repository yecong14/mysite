from . import views
from django.conf.urls import url

urlpatterns = [
        url(r'^login/$',views.user_login,name='user_login'),
    ]

