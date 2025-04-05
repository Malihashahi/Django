from django.shortcuts import render , HttpResponse
users = [
{ 
     'username' :'bahar',
     'name' : 'malihabahar',
     'lastname': 'shahi',
     'phone' : '093883883'

}
]

def profile(request , username):
      print(username)
      return  render(request ,"accounts_app/profile.html", context={"name": username})
def info(request):
    return render(request  ,"accounts_app/info.html")
