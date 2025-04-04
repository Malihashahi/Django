from django.shortcuts import render , HttpResponse


def profile(request , username):
      print(username)
      return  render(request ,"accounts_app/profile.html", context={"name": username})
def info(request):
    return render(request  ,"accounts_app/info.html")
