from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserForm
from .models import User


# Create your views here.
def home(request):
    return render(request,'one.html')

def register(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=UserForm()
    return render(request,'register.html',{'form':form})

def tableview(request):
    users=User.objects.all()
    return render(request,'tableview.html',{'users':users})

def user_delete(request,id):
    user=get_object_or_404(User,id=id)
    user.delete()
    return redirect('tableview') 

def user_edit(request, id): 
    if request.method=='POST':
        user=get_object_or_404(User, id=id)
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tableview')
    else:
        form=UserForm()
    return render(request,'editview.html',{'form':form}) 

