
from django.contrib import admin
from django.urls import path
from django.urls import path, include # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), 
    path("", include("blog.urls")), 
]
