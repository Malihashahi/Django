from django.shortcuts import render , HttpResponse
users = ['bahar', 'hadid' , 'nergis','sam']
blocked_users = ['nergis' ,'hadid']

def profile(request , username):
    if username in users:
         if username in blocked_users:
             return HttpResponse(f"{username} is blocked")
         else:
            return HttpResponse(f"this is {username} s profile")
    else:
        return HttpResponse('This username is not register')




def codeyade(request):
    return HttpResponse("this is  codeyade webseite")
