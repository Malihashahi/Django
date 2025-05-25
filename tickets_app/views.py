from django.shortcuts import render

def add_ticket(request):
    return render(request ,'tickets_app/add_ticket.html')
 