from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages

# Create your views here.
def show_data(request):
    students = Student.objects.all()
    if request.method=="POST" and request.FILES:
        image = request.FILES["image"]
        name = request.POST["name"]
        address = request.POST["address"]
        level = request.POST["level"]
        slug = request.POST["slug"]
        std = Student(name=name,address=address,level=level,image=image,slug=slug)
        std.save()
        messages.success(request, "Successfully created !!!")
        return redirect('show_data')

    return render(request, 'show_data.html', {'students': students})


def update_data(request,slug):
    if request.method=="POST" and request.FILES:
        std = Student.objects.get(slug=slug)
        std.image = request.FILES['image']
        std.name = request.POST["name"]
        std.address = request.POST["address"]
        std.level = request.POST["level"]
        std.slug = request.POST["slug"]
        std.save()
        messages.success(request, "Successfully updated !!!")
        return redirect('show_data')
    else:
        std = Student.objects.get(slug=slug)

    return render(request, 'update_data.html', {'std': std})

def delete_data(request,slug):
    std = Student.objects.get(slug=slug)
    std.delete()
    return redirect('show_data')

