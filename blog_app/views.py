from django.shortcuts import render ,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello here maliha ")
    

def contactus(request):
    return HttpResponse("send your idea")