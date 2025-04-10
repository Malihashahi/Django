from django.shortcuts import render , HttpResponse
from django.http import Http404
users = [
{ 
     'username' :'bahar',
     'name' : 'malihabahar',
     'lastname': 'shahi',
     'phone' : '093883883'

},
{ 
     'username' :'bahar',
     'name' : 'malihabahar',
     'lastname': 'shahi',
     'phone' : '093883883'

},
{ 
     'username' :'hadid',
     'name' : 'sediqa',
     'lastname': 'golobi',
     'phone' : '09388883883'

},{ 
     'username' :'majidjan',
     'name' : 'majid',
     'lastname': 'hamide',
     'phone' : '07990003883'

}


]
def userlist(request):
    users_list = users
    return render(request , 'accounts_app/user_list.html',context={'user_list' : users_list})

def profile(request , username):
    for user in users:
         if user['username'] == username:
            return render( request , 'accounts_app/profile.html',context={'user': user})
    raise Http404('this user is not found')
def info(request):
    return render(request  ,"accounts_app/info.html")
