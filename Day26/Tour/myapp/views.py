from django.shortcuts import render,redirect
from .models import Tour
from myapp.forms import Tour_Form


# Create your views here.

def show_data(request):
    if request.method == "POST":
        form = Tour_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_data')
    else:
        form=Tour_Form()
        data=Tour.objects.all()
            
        return render(request,'tour.html',{'form':form, 'datas':data})
        
def edit_data(request,id):
    if request.method=="POST":
        edata = Tour.objects.get(id=id)
        formdata = Tour_Form(request.POST,instance=edata)
        formdata.is_valid()
        formdata.save()
        return redirect('show_data')
    else:
        edata = Tour.objects.get(id=id)
        form = Tour_Form(instance=edata)
        data=Tour.objects.all()
        return render(request,'edit_tour.html',{'form':form, 'datas':data, 'edata':edata})

        

def delete_data(request,id):
    data = Tour.objects.get(id=id)
    data.delete()
    return redirect('show_data')


    
