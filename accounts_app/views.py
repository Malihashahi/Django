from django.shortcuts import render , HttpResponse


def profile(request , username):
      return  render(request ,"accounts_app/profile.html")
def codeyade(request):
    return HttpResponse("this is  codeyade webseite")
