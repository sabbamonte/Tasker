from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist, ValidationError
import time
import datetime

from .models import User, Tasks, Subject, URL, Notes

@login_required(login_url='/login')
def index(request):
    if request.method == "GET":
        today = datetime.datetime.now().date()
        tasks = Tasks.objects.filter(user=request.user, checked=False).order_by('-deadline').reverse()
        subjects = Subject.objects.filter(user=request.user)
        categories = Subject.objects.all()
        category = []
        for cat in categories:
            if cat.category not in category:
                category.append(cat.category)
        for task in tasks:
            days_left =  task.deadline - datetime.datetime.now().date()
            if today == task.deadline:
                return render(request, "Tasker/index.html", {"tasks":tasks, "subjects":subjects, "task":task, "category":category})
            else:
                return render(request, "Tasker/index.html", {"tasks":tasks, "subjects":subjects, "task":task, "days_left": days_left.days, "category":category})
        
        return render(request, "Tasker/index.html", {"tasks":tasks, "subjects":subjects, "category":category})


def login_view(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "Tasker/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "Tasker/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "Tasker/register.html", {
                "message": "Passwords must match."
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "Tasker/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "Tasker/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

@login_required
@csrf_exempt
def add(request):
    if request.method == "GET":
        tasks = Tasks.objects.filter(user=request.user).values()
        return JsonResponse({"tasks": list(tasks)})
    
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        if data.get('link') is not None:
            url = URL()
            data = json.loads(request.body.decode("utf-8"))
            url.name = data.get('name')
            url.subject = data.get('subject')
            url.links = data.get('link')
            url.save()
            return JsonResponse({"message": "Post updated successfully."}, status=201)

        if data.get('note') is not None:
            note = Notes()
            data = json.loads(request.body.decode("utf-8"))
            note.subject = data.get('subject')
            note.note = data.get('note')
            if not data.get('note'):
                return JsonResponse({"error": "Enter your note."}, status=400)
            note.user = request.user
            note.save()
            return JsonResponse({"message": "Post updated successfully."}, status=201)
        
        else:
            task = Tasks()
            task.user = request.user
            task.task = data.get('task')
            if not data.get('task'):
                return JsonResponse({"error": "Enter your task."}, status=400)
            task.deadline = data.get('deadline')
            if not data.get('deadline'):
                return JsonResponse({"error": "Enter your deadline."}, status=400)
            task.save()
            return JsonResponse({"message": "Post updated successfully."}, status=201)

@login_required
@csrf_exempt
def check(request, task_id):
    task = Tasks.objects.filter(user=request.user, id=task_id).values()

    if request.method == "GET":
        return JsonResponse({"task": list(task)})

    if request.method == "PUT":
        task = Tasks.objects.get(user=request.user, id=task_id)
        data = json.loads(request.body.decode("utf-8"))
        if data.get('checked') is not None:
            task.checked = data['checked']
        task.save()
        return HttpResponse(status=204)

@login_required
@csrf_exempt
def archive(request):
    if request.method == "GET":
        archived = Tasks.objects.filter(user=request.user, checked=True)
        if not archived:
            return render(request, "Tasker/archive.html", {"message": "No Tasks"})
        else:
            return render(request, "Tasker/archive.html", {"archived":archived})

    if request.method == "POST":
        Tasks.objects.filter(checked=True).delete()
        return HttpResponseRedirect(reverse("index"))

@login_required
@csrf_exempt
def delete(request, task_id):
    Tasks.objects.get(user=request.user, id=task_id).delete()
    return JsonResponse({"message": "Post updated successfully."}, status=201)

@login_required
@csrf_exempt
def delete_link(request, subject, link_id):
    if request.method == "GET":
        url = URL.objects.get(subject=subject, id=link_id).values()
        return JsonResponse({"task": list(url)})

    elif request.method == "DELETE":
        try:
            URL.objects.get(subject=subject, id=link_id).delete()
        except ObjectDoesNotExist:
            Notes.objects.get(user=request.user, subject=subject, id=link_id).delete()
        return JsonResponse({"message": "Post updated successfully."}, status=201)

@login_required
@csrf_exempt
def subjects(request):
    if request.method == "GET":
        subjects = Subject.objects.filter(user=request.user)
        return render(request, "Tasker/subjects.html", {'subjects': subjects})

    if request.method == "POST":
        new_subject = Subject()

        new_subject.user = request.user
        new_subject.subject = request.POST['title']
        if not new_subject.subject:
            return render(request, "Tasker/subjects.html", {
                "message": "Please enter the name of the subject"
            })
        new_subject.category = request.POST['category']
        if not request.POST['category']:
            new_subject.category = None

        double_title = Subject.objects.filter(user=request.user, subject=new_subject.subject)
        if double_title:
            return render(request, "Tasker/subjects.html", {
                "message": "A subject with that name already exists"
            })

        new_subject.save()

        URL.objects.bulk_create([
        URL(subject=new_subject.subject, links=request.POST['url1'], name=request.POST['name1']),
        URL(subject=new_subject.subject, links=request.POST['url2'], name=request.POST['name2']),
        URL(subject=new_subject.subject, links=request.POST['url3'], name=request.POST['name3']),
        ])
        
        URL.objects.filter(links='').delete()

        return HttpResponseRedirect(reverse("index"))

@login_required      
@csrf_exempt
def subject(request, subject):
    if request.method == "GET":
        subject = Subject.objects.get(user=request.user, subject=subject)
        links = URL.objects.filter(subject=subject.subject)
        notes = Notes.objects.filter(user=request.user, subject=subject.subject)
        return render(request, "Tasker/subject.html", {'subject': subject, 'links':links, 'notes':notes})
    
    if request.method == "POST":
        Subject.objects.get(user=request.user, subject=subject).delete()
        Notes.objects.filter(user=request.user, subject=subject).delete()
        return HttpResponseRedirect(reverse("index"))
        
@login_required
@csrf_exempt
def edit_note(request, subject, note_id):
    if request.method == "GET":
        note = Notes.objects.filter(user=request.user, subject=subject, id=note_id).values()
        return JsonResponse({"task": list(note)})

    if request.method == "PUT":
        new_note = Notes.objects.get(user=request.user, id=note_id)
        data = json.loads(request.body.decode("utf-8"))
        new_note.note = data.get('note')
        if not data.get('note'):
                Notes.objects.get(user=request.user, id=note_id).delete()
                return JsonResponse({"message": "Note edited successfully."}, status=201)
        new_note.save()
        return JsonResponse({"message": "Note edited successfully."}, status=201)

@login_required
def filter(request, category):
    if request.method == "GET":
        filters = Subject.objects.filter(category=category.capitalize()).values()
        if category == "All":
            filters = Subject.objects.all().values()

        return JsonResponse({"filters":list(filters)})
        









