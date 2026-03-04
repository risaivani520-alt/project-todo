from django.shortcuts import render,redirect,get_object_or_404
from .models import Users,Todo
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import logout

def signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if Users.objects.filter(email=email).exists():
             return render(request,'signup.html',{'error':'Already Registered go to login  '})
        Users.objects.create(
            name=name,
            email=email,
            password=make_password(password)
    
        )
        return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method=='POST':
        uname=request.POST.get('name')
        upassword=request.POST.get('password')
        try:
            user=Users.objects.get(name=uname)
            if check_password(upassword,user.password):
                request.session['sessionId']=user.id
                request.session['seesionName']=user.name
                return redirect('todo')
            else:
                error='Invalid name and password'
                return render(request,'login.html',{'error':error})
            
        except Users.DoesNotExist:
            error='Login detail not found'
            return render(request,'login.html',{'error':error})

    return render(request,'login.html')

def todo(request):
    if request.method=='POST':
        title=request.POST.get('title')
        user_id=request.session.get('sessionId')
        user=Users.objects.get(id=user_id)
        Todo.objects.create(
            title=title,
            user=user
        )
    user_id=request.session.get('sessionId')
    todo=Todo.objects.filter(user_id=user_id)
         
    return render(request,'todo.html',{'todo':todo})


def edit(request,sno):
    todo=get_object_or_404(Todo,sno=sno,user_id=request.session.get('sessionId'))
    if request.method=='POST':
        todo.title=request.POST.get('title')
        todo.save()
        return redirect('todo')    
    return render(request,'edit.html',{'todo':todo})

def delete(request,sno):
    todo=get_object_or_404(Todo,sno=sno,user_id=request.session.get('sessionId'))
    todo.delete()
    return redirect('todo')    

def logoutuser(request):
    logout(request)
    return redirect('login')

# Create your views here.
