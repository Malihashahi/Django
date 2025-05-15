from django.shortcuts import render, HttpResponse



def home(request):
    return render(request, "blog_app/blog.html")



def contactus(request):
    return HttpResponse('Hi This Is Contact us Page')