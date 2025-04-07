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
     'username' :'sam',
     'name' : 'samirbayan',
     'lastname': 'bayan',
     'phone' : '07990003883'

}


]

def profile(request , username):
    for user in users:
         if user['username'] == username:
            return render( request , 'accounts_app/profile.html',context={'user': user})
    raise Http404('this user is not found')
def info(request):
    return render(request  ,"accounts_app/info.html")
