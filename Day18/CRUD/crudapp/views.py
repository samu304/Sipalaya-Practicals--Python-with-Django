from django.shortcuts import render,redirect    
from django.contrib import messages

from .models import Student

# Create your views here.
def show_data(request):
    students = Student.objects.all()
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['text']
        std = Student(first_name =firstname,last_name = lastname,email=email,phone=phone,message=message)
        std.save()

        messages.success(request, "Successfully created !!! ")
        return redirect('show_data')

    return render(request, 'crudapp/show_data.html', {'students':students})


def update_data(request,id):
    if request.method == "POST":
        std = Student.objects.get(id=id)
        std.first_name = request.POST['first_name']
        std.last_name = request.POST['last_name']
        std.email = request.POST['email']
        std.phone = request.POST['phone']
        std.message = request.POST['text']
        std.save()
        
        messages.success(request, "Successfully updated !!! ")
        return redirect('show_data')
    else:
        std = Student.objects.get(id=id)

    return render(request, 'crudapp/update_data.html', {'std':std})

def delete_data(request,id):
    std = Student.objects.get(id=id)
    std.delete()
    return redirect('show_data')