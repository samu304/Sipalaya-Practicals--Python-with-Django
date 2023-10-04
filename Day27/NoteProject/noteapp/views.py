from django.shortcuts import render,redirect
from .models import Task
from django.contrib import messages

# Create your views here.
def show(request):
    datas = Task.objects.all()
    if request.method == "POST":
        text = request.POST['content']
        data = Task(content=text)
        data.save()
        messages.success(request,"Added Successfully !")

    return render(request, 'task.html', {'tasks':datas})

def delete_note(request, id):
    data = Task.objects.get(id=id)
    data.delete()
    messages.success(request, "Deleted Successfully ! ")
    return redirect('show_note')

def update_note(request, id):
    if request.method == "POST":
        data = Task.objects.get(id=id)
        data.content = request.POST['content']
        data.save()
        messages.success(request, "Updated Successfully !")
        return redirect('show_note')
    else:
        data = Task.objects.get(id=id)
    return render(request, 'update.html', {'task':data})