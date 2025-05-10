from django.shortcuts import render ,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Blog App ")
    

def contactus(request):
    return HttpResponse("send your idea for us ")