from django.urls import path
from . import views


urlpatterns = [
    path('maliha', views.maliha_bahar),
    path('codeyade', views.codeyade),
    
    ]



