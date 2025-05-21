from django.shortcuts import render
from .models import Course

def courses_list(request):
    courses = Course.objects.all()

    return render(request , "courses_app/courses_list.html", context={'courses' : courses})



def course_detail(request ,id):
    course = Course.objects.get(id=id)
    course.views += 1
    if course.statution == True:
         course.statution = False
    else:
        course.statution = True


    course.save()
    return render(request ,"courses_app/course_detail.html" , context={'course':course} )




def add_course(request):
    name = request.Get.get('name')
    return render(request , 'courses_app/add_course.html')