from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import user_details,Task
from django.contrib.auth import login as auth_login,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['confirmPassword']
        if User.objects.filter(username = username).exists():
            return render(request,'tasks/signup.html',{'err_msg':'User already Exists!!'})
        if password == c_password:
            hash_password = make_password(password)
        user = User.objects.create_user(username=username,email=email,password=password)
        user_details_instances = user_details.objects.create(
            author = user,
            username=username,
            firstname=firstname,
            lastname=lastname,
            email=email,
            password=hash_password,  # Use the hashed password
            c_password=hash_password
        )
        user_details_instances.save()
        return redirect('/login')
    return render(request,'tasks/signup.html')
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/tasks')
        else:
            return redirect('/login')#render(request,'tasks/login.html',{'err':'Invalid User'})
    return render(request,'tasks/login.html')

def tasks(request):
    user = request.user
    get_task = Task.objects.filter(user = user).order_by('-time')
    return render(request,'tasks/tasks.html',{'tasks':get_task})
@login_required
def create_task(request):
    
    if request.method == "POST":
        user = request.user
        task_name = request.POST['taskName']
        description = request.POST['description']
        
        task = Task(user=user,title=task_name,description=description)
        task.save()
        return redirect('/tasks')
    
    return render(request,'tasks/task.html')

def mark_finished(request,task_id):
    if request.method == "POST":
        try:
            task_finish = Task.objects.get(pk = task_id,user = request.user)
            task_finish.completed = True
            task_finish.progress = 'Completed'
            task_finish.save()
        except Task.DoesNotExist:
            pass
    return redirect('/tasks')
            
def delete_task(request,task_id):
    user = request.user
    try:
        task_deleted = Task.objects.get(pk = task_id,user=user)
        task_deleted.delete()
    except Task.DoesNotExist:
        pass
        
    return redirect('/tasks')
