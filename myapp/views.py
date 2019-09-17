from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def home(request):
    return render(request, 'home.html')

    #쿼리셋과 메소드의 형식
    #모델.쿼리셋(odject).메소드
def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html',{'blog':blog_detail})   
 
def achievement(request):
    return render(request, 'achievement.html')

def electrospinning(request):
    blogs = Blog.objects
    return render(request, 'electrospinning.html', {'blogs': blogs})

def external(request):
    return render(request, 'external.html')

def Lab_home(request):
    return render(request, 'Lab_home.html')

def microneedle(request):
    return render(request, 'microneedle.html')

def Not_subject(request):
    return render(request, 'Not_subject.html')

def result(request):
    return render(request, 'result.html')