import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from .models import Todo, Category


@csrf_exempt
def all_todo(request):
    all_todo=Todo.objects.all()
    all_todo_serialized=serializers.serialize('json', all_todo)
    all_todo_json=json.loads(all_todo_serialized)
    data= json.dumps(all_todo_json)
    return HttpResponse(data)

@csrf_exempt
def all_cat(request):
    all_cat=Category.objects.all()
    all_cat_serialized=serializers.serialize('json', all_cat)
    all_cat_json=json.loads(all_cat_serialized)
    data= json.dumps(all_cat_json)
    return HttpResponse(data)


@csrf_exempt
def insert_cat(request):
    try:
        name=request.POST.get('name')
        cat_instance = Category()
        cat_instance.name = name
        cat_instance.save()
        return HttpResponse("200")
    except:
        return HttpResponse("Not ok")

@csrf_exempt
def insert_todo(request):
    try:
        title= request.POST.get('title')
        description= request.POST.get('description')
        avatar= request.POST.get('avatar')
        priority= request.POST.get('priority')
        date= request.POST.get('date')
        start_time= request.POST.get('start_time')
        finish_time= request.POST.get('finish_time')
        # category= serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        category= Category.objects.get(id='id')

        todo_instance=Todo()
        todo_instance.title=title
        todo_instance.description=description
        todo_instance.avatar=avatar
        todo_instance.priority=priority
        todo_instance.date=date
        todo_instance.start_time=start_time
        todo_instance.finish_time=finish_time
        todo_instance.category=category
        todo_instance.save()
        return HttpResponse("200")
    except :
        return HttpResponse("Not ok")

@csrf_exempt
def update_cat(request):
    try:
        id=request.POST.get('id')
        name= request.POST.get('name')
        Category.objects.filter(id=id).update(name=name)
        return HttpResponse("200")
    except:
        return HttpResponse("Not Ok")

@csrf_exempt
def update_todo(request):
    try:
        id=request.POST.get('id')
        description = request.POST.get('description')
        avatar = request.POST.get('avatar')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        finish_time = request.POST.get('finish_time')
        category = request.POST.get('name')
        title= request.POST.get('title')
        Todo.objects.filter(id=id).update(title=title, description=description, avatar=avatar,
                                          priority=priority, date=date, start_time=start_time, finish_time=finish_time,
                                          category=category)
        return HttpResponse("200")
    except:
        return HttpResponse("Not Ok")

@csrf_exempt
def delete_cat(request):
    try:
        id=request.POST.get('id')

        Category.objects.filter(id=id).delete()
        return HttpResponse("200")
    except:
        return HttpResponse("Not Ok")

@csrf_exempt
def delete_todo(request):
    try:
        id=request.POST.get('id')

        Todo.objects.filter(id=id).delete()
        return HttpResponse("200")
    except:
        return HttpResponse("Not Ok")