from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializers
from rest_framework import status

# Create your views here.
def student_api(request, pk=None):
    if request.method == "GET":
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many = True)
        return Response(serializer.data)
    