
from django.contrib import admin
from django.urls import path
from djangoform import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_form, name="student_form"),
]
