import calendar
import datetime
import json
import time
from datetime import datetime

from django.core import serializers
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Todo, Category, Subset

#___________________________________________________functions__________________________________________________

def todo_insert_validation(start_time, finish_time,date):
    if start_time == finish_time:
        overlap = True
        return overlap
    elif start_time > finish_time:
        overlap = True
        return overlap
    elif Todo.objects.filter(date=date).exists():
        all = Todo.objects.filter(date=date)
        for task in all:
            start_time = datetime.strptime(start_time, '%H:%M:%S').time()
            finish_time = datetime.strptime(finish_time, '%H:%M:%S').time()
            # inner limitations
            if start_time >= task.start_time and start_time <= task.finish_time:
                overlap=True
                return overlap
            #inner limitations
            elif finish_time >= task.start_time and finish_time <= task.finish_time:
                overlap=True
                return overlap
            # outer limitations
            elif start_time <= task.start_time and finish_time >= task.finish_time:
                overlap=True
                return overlap
        else:
            overlap = False
            return overlap


def curent_week_calc():
    start_day_of_week = 5
    d = datetime.datetime.today().weekday()
    delta_d = d - start_day_of_week
    if delta_d == 0:
        start_date_of_week = datetime.date.today()
        finish_date_of_week = start_date_of_week + datetime.timedelta(days=6)
        return(start_date_of_week, finish_date_of_week)
    elif delta_d == 1:
        start_date_of_week = datetime.date.today() - datetime.timedelta(days=1)
        finish_date_of_week = start_date_of_week + datetime.timedelta(days=6)
        return(start_date_of_week, finish_date_of_week)
    elif delta_d == -5:
        start_date_of_week = datetime.date.today() - datetime.timedelta(days=2)
        finish_date_of_week = start_date_of_week + datetime.timedelta(days=6)
        return(start_date_of_week, finish_date_of_week)
    elif delta_d == -4:
        start_date_of_week = datetime.date.today() - datetime.timedelta(days=3)
        finish_date_of_week = start_date_of_week + datetime.timedelta(days=6)
        return(start_date_of_week, finish_date_of_week)
    elif delta_d == -3:
        start_date_of_week = datetime.date.today() - datetime.timedelta(days=4)
        finish_date_of_week = start_date_of_week + datetime.timedelta(days=6)
        return(start_date_of_week, finish_date_of_week)
    elif delta_d == -2:
        start_date_of_week = datetime.date.today() - datetime.timedelta(days=5)
        finish_date_of_week = start_date_of_week + datetime.timedelta(days=6)
        return(start_date_of_week, finish_date_of_week)
    elif delta_d == -1:
        start_date_of_week = datetime.date.today() - datetime.timedelta(days=6)
        finish_date_of_week = start_date_of_week + datetime.timedelta(days=6)
        return (start_date_of_week, finish_date_of_week)


def next_week_calc():
    start_date_of_week=curent_week_calc()[1]+datetime.timedelta(days=1)
    finish_date_of_week = start_date_of_week + datetime.timedelta(days=6)
    return (start_date_of_week, finish_date_of_week)


def last_week_calc():
    finish_date_of_week=curent_week_calc()[0]-datetime.timedelta(days=1)
    start_date_of_week = finish_date_of_week - datetime.timedelta(days=6)
    return (start_date_of_week, finish_date_of_week)
##  ____________________________________________VIEW _________________________________________
@csrf_exempt
def all_todo(request):
    try:
        all_todo=Todo.objects.all()
        all_todo_serialized=serializers.serialize('json', all_todo)
        all_todo_json=json.loads(all_todo_serialized)
        data= json.dumps(all_todo_json)
        return HttpResponse(data)
    except:
        return HttpResponse("Not Ok")


@csrf_exempt
def all_subset(request):
    try:
        all_sub=Subset.objects.all()
        all_sub_serialized=serializers.serialize('json', all_sub)
        all_sub_json=json.loads(all_sub_serialized)
        data= json.dumps(all_sub_json)
        return HttpResponse(data)
    except:
        return HttpResponse("Not Ok")


@csrf_exempt
def all_cat(request):
    try:
        all_cat=Category.objects.all()
        all_cat_serialized=serializers.serialize('json', all_cat)
        all_cat_json=json.loads(all_cat_serialized)
        data= json.dumps(all_cat_json)
        return HttpResponse(data)
    except:
        return HttpResponse("Not Ok")
## ________________________________________FILTERED VIEW ________________________________________


@csrf_exempt
def all_todo_filtered_cat(request):
    try:
        category_id = request.POST.get('category_id')
        all_todo = Todo.objects.filter(category=category_id)
        all_todo_serialized=serializers.serialize('json', all_todo)
        all_todo_json=json.loads(all_todo_serialized)
        data= json.dumps(all_todo_json)
        return HttpResponse(data)
    except:
        return HttpResponse("Not Ok")

@csrf_exempt
def all_subset_filtered_todo(request):
    try:

        all_sub_serialized=serializers.serialize('json', all_todo)
        all_sub_json=json.loads( all_sub_serialized)
        data= json.dumps(all_sub_json)
        return HttpResponse(data)
    except:
        return HttpResponse("Not Ok")


@csrf_exempt
def all_todo_filtered_today(request):
    try:
        current_Date = datetime.datetime.today()
        all_todo = Todo.objects.filter(date=current_Date)
        all_todo_serialized=serializers.serialize('json', all_todo)
        all_todo_json=json.loads(all_todo_serialized)
        data= json.dumps(all_todo_json)
        return HttpResponse(data)
    except:
        return HttpResponse("Not Ok")


@csrf_exempt
def all_todo_filtered_yesterday(request):
    try:
        previous_day_date = datetime.datetime.today() - datetime.timedelta(days=1)
        all_todo = Todo.objects.filter(date=previous_day_date)
        all_todo_serialized=serializers.serialize('json', all_todo)
        all_todo_json=json.loads(all_todo_serialized)
        data= json.dumps(all_todo_json)
        return HttpResponse(data)
    except:
        return HttpResponse("Not Ok")


@csrf_exempt
def all_todo_filtered_current_week(request):
    try:
        start_date_of_week=curent_week_calc()[0]
        finish_date_of_week=curent_week_calc()[1]
        all_todo = Todo.objects.filter(date__gte=start_date_of_week , date__lte=finish_date_of_week)
        all_todo_serialized = serializers.serialize('json', all_todo)
        all_todo_json = json.loads(all_todo_serialized)
        data = json.dumps(all_todo_json)
        return HttpResponse(data)

    except:
        return HttpResponse("Not Ok")


@csrf_exempt
def all_todo_filtered_next_week(request):
    try:
        start_date_of_week=next_week_calc()[0]
        finish_date_of_week=next_week_calc()[1]
        all_todo = Todo.objects.filter(date__gte=start_date_of_week , date__lte=finish_date_of_week)
        all_todo_serialized = serializers.serialize('json', all_todo)
        all_todo_json = json.loads(all_todo_serialized)
        data = json.dumps(all_todo_json)
        return HttpResponse(data)

    except:
        return HttpResponse("Not Ok")


@csrf_exempt
def all_todo_filtered_last_week(request):
    try:
        start_date_of_week=last_week_calc()[0]
        finish_date_of_week=last_week_calc()[1]
        all_todo = Todo.objects.filter(date__gte=start_date_of_week , date__lte=finish_date_of_week)
        all_todo_serialized = serializers.serialize('json', all_todo)
        all_todo_json = json.loads(all_todo_serialized)
        data = json.dumps(all_todo_json)
        return HttpResponse(data)

    except:
        return HttpResponse("Not Ok")


@csrf_exempt
def all_todo_filtered_tomorrow(request):
    try:
        next_day_date = datetime.datetime.today() + datetime.timedelta(days=1)
        all_todo = Todo.objects.filter(date=next_day_date)
        all_todo_serialized=serializers.serialize('json', all_todo)
        all_todo_json=json.loads(all_todo_serialized)
        data= json.dumps(all_todo_json)
        return HttpResponse(data)
    except:
        return HttpResponse("Not Ok")


@csrf_exempt
def all_todo_filtered_status(request):
    try:
        status = request.POST.get('status')
        all_todo= Todo.objects.filter(status=status)
        all_todo_serialized=serializers.serialize('json', all_todo)
        all_todo_json=json.loads(all_todo_serialized)
        data= json.dumps(all_todo_json)
        return HttpResponse(data)

    except:
        return  HttpResponse("Not Ok")


@csrf_exempt
def all_todo_filtered_date(request):
    try:
        date = request.POST.get('date')
        all_todo= Todo.objects.filter(date=date)
        all_todo_serialized=serializers.serialize('json', all_todo)
        all_todo_json=json.loads(all_todo_serialized)
        data= json.dumps(all_todo_json)
        return HttpResponse(data)

    except:
        return  HttpResponse("Not Ok")


@csrf_exempt
def all_todo_filtered_date_range(request):
    try:
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        all_todo= Todo.objects.filter(date__gte=date1 , date__lte=date2)
        all_todo_serialized=serializers.serialize('json', all_todo)
        all_todo_json=json.loads(all_todo_serialized)
        data= json.dumps(all_todo_json)
        return HttpResponse(data)

    except:
        return  HttpResponse("Not Ok")
## ______________________________________________INSERT_______________________________________________


@csrf_exempt
def insert_cat(request):
    try:
        name = request.POST.get('name')
        cat_instance = Category()
        cat_instance.name = name
        if Category.objects.filter(name=name).exists():
            return HttpResponse ("there is duplicate value for Category")
        else:
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
        status= request.POST.get('status')
        start_time= request.POST.get('start_time')
        finish_time= request.POST.get('finish_time')
        due_date= request.POST.get('due_date')
        progress= request.POST.get('progress')
        category= Category.objects.get(id=request.POST.get('category_id'))

        todo_instance=Todo()
        todo_instance.title=title
        todo_instance.description=description
        todo_instance.avatar=avatar
        todo_instance.priority=priority
        todo_instance.date=date
        todo_instance.status=status
        todo_instance.start_time=start_time
        todo_instance.finish_time=finish_time
        todo_instance.due_date_time=due_date
        todo_instance.progress=progress
        todo_instance.category=category

        # time validation
        overlap=todo_insert_validation(start_time, finish_time, date)
        if overlap == True:
            return HttpResponse("Overlapped")
        else:
            todo_instance.save()
            return HttpResponse("200")

    except :
        return HttpResponse("Not ok")


@csrf_exempt
def insert_subset(request):
        title= request.POST.get('title')
        priority= request.POST.get('priority')
        status= request.POST.get('status')
        todo= Todo.objects.get(id=request.POST.get('todo_id'))

        subset_instance=Subset()
        subset_instance.title=title
        subset_instance.priority=priority
        subset_instance.status=status
        subset_instance.todo=todo
        subset_instance.save()
        return HttpResponse("200")




## ________________________________________UPDATE_______________________________________________


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
        status = request.POST.get('status')
        due_date= request.POST.get('due_date')
        start_time = request.POST.get('start_time')
        finish_time = request.POST.get('finish_time')
        category= Category.objects.get(id=request.POST.get('category_id'))
        progress= request.POST.get('progress')
        title= request.POST.get('title')
        if start_time == finish_time:
            return HttpResponse("finish time should be greater than start time")
        elif progress== "100":
            Todo.objects.filter(id=id).update(title=title, description=description, avatar=avatar,
                                              priority=priority, date=date, status="D", start_time=start_time,
                                              finish_time=finish_time,due_date=due_date,
                                              progress=progress, category=category)
            return HttpResponse("200")
        else:
            Todo.objects.filter(id=id).update(title=title, description=description, avatar=avatar,
                                              priority=priority, date=date,status=status, start_time=start_time, finish_time=finish_time,
                                              due_date=due_date,progress=progress, category=category)
            return HttpResponse("200")
    except:
        return HttpResponse("Not Ok")

## _________________________________________________DELETE________________________________________


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