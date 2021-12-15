# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from .models import Logs
from .helpers import send_forget_pass
from django.contrib.auth.models import User


# Create your views here.'
# from homep.forms import Loginform

def homep(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        obj = Logs.objects.filter(username=name, password=password)
        if obj:
            request.session['name'] = name
            return redirect('../welcome')
        else:
            print("NOPE")
            return render(request, 'homep/homep.html', {'error': "**User do not Exist"})
    elif request.session.has_key('name'):
        return redirect('../welcome')

    return render(request, 'homep/homep.html')

def regist(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj = Logs.objects.create(name=name,username=email,password=password)
        obj.save()
        return render(request,'homep/regist.html',{'message':"Signup Successfully!!"})
    return render(request,'homep/regist.html')

def homepwel(request):
    if request.session.has_key('name'):
        name = request.session['name']
        obj = Logs.objects.filter(username=name)
        for k in obj:
            return render(request,'homep/welocme.html',{'name':k.name})
    return HttpResponse("You need to Login first")

def logout(request):
    if request.session.has_key('name'):
        try:
            del request.session['name']
            return redirect('home')
        except:
            return redirect('home')
import uuid
def forgot(request):
    if request.method == "POST":
        email = request.POST.get("name")
        if Logs.objects.filter(username=email).exists():
            # obj = Logs.objects.get(username=name)
            # print("check",obj)
            token = str(uuid.uuid4())
            print(token)
            send_forget_pass(email,token)
        else:
            return render(request, 'forgotpass.html',{"error":"User not Exist"})

    return render(request,'forgotpass.html')


def change_pass(request,token):
    if request.method == "POST":
        username = request.POST.get("email")
        print(username)
        pass1 = request.POST.get("pass1")
        obj = Logs.objects.filter(username = username)
        print(obj)
    return render(request,'changepass.html')











