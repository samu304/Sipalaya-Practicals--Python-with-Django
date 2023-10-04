
from django.contrib import admin
from django.urls import path

from generic import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('std/', view.StudentListView.as_view(), name="student_list")
]
