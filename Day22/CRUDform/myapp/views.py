from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from django.http import HttpResponse

# Create your views here.
def  show_data(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully added !!! ")
        else:
            return HttpResponse("Form is not valid")
    else:
        form = StudentForm()
        students = Student.objects.all()
    return render(request, 'show_data.html', {'form': form, 'students':students})


# views to delete a data
def delete_data(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return HttpResponse("Successfully Deleted !!! ")

# views to update the data
def update_data(request, id):
    std = Student.objects.get(id=id)
    if request.method=="POST":
        std = Student.objects.get(id=id)
        form = StudentForm(request.POST, instance=std)
        if form.is_valid():
            form.save()
            return HttpResponse("Updates Successfully !!! ")
        else:
            return HttpResponse("Invalid Form Inputs ")
    else:
        form = StudentForm(instance=std)
    return render(request, 'update_data.html', {'form':form})