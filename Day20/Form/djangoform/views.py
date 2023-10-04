from django.shortcuts import render
from .forms import Student

# Create your views here.

def student_form(request):
    stud = Student()
    return render(request, "index.html", {"form": stud })