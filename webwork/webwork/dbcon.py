from itertools import count
from django.http import HttpResponse
from django.shortcuts import render

from User.models import User


def addUser(request):
    username = request.POST.get('username')
    if(username == "" or username is None):
        username = request.GET.get('username')
        if(username == "" or username is None):
            return render(request,'logup.html',{'error':'用户名不能为空'})
    password = request.POST.get('password')
    if(password == "" or password is None):
        password = request.GET.get('password')
        if(password == "" or password is None):
            return render(request,'logup.html',{'error':'密码不能为空'})
    count = User.objects.filter(name=username).count()
    if(count < 1):
        user = User(name=username,password=password)
        user.save()
        return render(request,'login.html')
    return render(request,'logup.html',{'error':'用户已存在'})

def logon(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    count = User.objects.filter(name=username).count()
    if(count<1):
        return render(request,'login.html',{'error':'用户不存在'})
    count = User.objects.filter(name=username,password=password).count()
    if(count<1):
        return render(request,'login.html',{'error':'密码错误'})
    return render(request,'index.html')