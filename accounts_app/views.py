from django.shortcuts import render , HttpResponse


def profile(request , username):
      return  render(request ,"accounts_app/profile.html")
def info(request):
    return render(request  ,"accounts_app/info.html")
