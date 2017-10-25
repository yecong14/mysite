from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$',views.blog_title,name='blog_title'),
        url(r'^blogarticles/(?P<article_id>\d+)/$',views.blog_articles,name='blog_articles'),
]
