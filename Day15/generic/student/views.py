from django.shortcuts import render
# for grnrric view
from django.views.generic.base import ListView
from .models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student