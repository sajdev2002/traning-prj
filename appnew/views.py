from django.shortcuts import render,redirect,get_object_or_404
from .forms import UserForm,login_form
from .models import User
from django.contrib import messages

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
    user=get_object_or_404(User, id=id)
    if request.method=='POST':
        form=UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('tableview')
    else:
        form=UserForm(instance=user)
    return render(request,'register.html',{'form':form}) 

def user_login(request):
    if request.method=='POST':
        form=login_form(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']

            try:
                user=User.objects.get(email=email)
                if user.password==password:
                    request.session['user_id']=user.id
                    request.session['email']=user.email
                    return redirect('tableview')
                else:
                    messages.error(request,'password is incorrect')
            except User.DoesNotExist:
                messages.error(request,'email is incorrect')
    else:
        form=login_form()
    return render(request,'login.html',{'form':form})

def user_logout(request):
    request.session.flush()
    return redirect('user_login')



