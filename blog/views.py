from django.shortcuts import render
from .models import BlogArticles

# Create your views here.
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,'blog/titles.html',{'blogs':blogs})

def blog_articles(request,article_id):
    blog = BlogArticles.objects.get(id=article_id)
    return render(request,'blog/articles.html',{'blog':blog})
