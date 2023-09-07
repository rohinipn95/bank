from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from reduction.models import Person, Branch,District


# Create your views here.
def index(request):
    return render(request,'firstpage.html')

def home(request):
    return render(request,'home.html')
def register(request):
    if request.method=='POST':
        US=request.POST['us']
        password = request.POST['pas1']
        password1= request.POST['pas2']
        if password==password1:
            if User.objects.filter(username=US).exists():
                messages.info(request ,"Username Taken")
                return redirect('reduction:register')
            else:
                user=User.objects.create_user(username=US,password=password)
                user.save()
                return redirect('reduction:login')
        else:
            messages.info(request,'password not matching')
            return  redirect('reduction:register')
        return redirect('home')
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return  redirect('reduction:newpage')
        else:
            messages.info(request,"invalid")
            return redirect('reduction:login')
    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return  redirect(request,'/')
def newpage(request):
    return render(request,'newpage.html')
def add(request):
    form = Person()
    if request.method == 'POST':
        form = Person(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')




    return render(request,'add.html')
def newuser(request):
    return render(request,'newuser.html')


