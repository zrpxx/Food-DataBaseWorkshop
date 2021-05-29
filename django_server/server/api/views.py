from django.db.models import QuerySet
from django.shortcuts import render

# Create your views here.
import json
from django.http import HttpResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import datetime


@csrf_exempt
def login(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))

    try:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.get(username=username)
    except KeyError:
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    except User.DoesNotExist:
        dic['status'] = "Failed"
        dic['message'] = "Wrong Username"
        return HttpResponse(json.dumps(dic))
    if user.password != password:
        dic['message'] = "Wrong Password"
        dic['status'] = "Failed"
        return HttpResponse(json.dumps(dic))
    else:
        dic['status'] = "Success"
        dic['user_id'] = user.uid
        dic['user_role'] = user.role
        return HttpResponse(json.dumps(dic))


@csrf_exempt
def register(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        user = User.objects.get(username=username)
    except KeyError:
        dic['status'] = "Failed"
        dic['message'] = "No Input"
        return HttpResponse(json.dumps(dic))
    except User.DoesNotExist:
        dic['status'] = "Success"
        now = datetime.datetime.now()
        newUser = User(username=username, password=password, role=role, register_time=now)
        newUser.save()
        return HttpResponse(json.dumps(dic))
    if user is not None:
        dic['status'] = "Failed"
        dic['message'] = "User exist"
        return HttpResponse(json.dumps(dic))


@csrf_exempt
def create(request):
    dic = {}
    if request.method == 'GET':
        dic['status'] = "Failed"
        dic['message'] = "Wrong Method"
        return HttpResponse(json.dumps(dic))
    try:
        pass
    except:
        pass