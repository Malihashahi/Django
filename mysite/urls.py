from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls')),
    path('accounts_app/',include('accounts_app.urls')),
    path('course/', include('courses_app.urls')),
    path('tickets/' , include('tickets_app.urls'))
]
