from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Tasks(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=200)
    deadline = models.DateField(null=True, blank=True)
    checked = models.BooleanField(default=False)

    def serialize(self):
        return {
            "user": self.user,
            "task": self.task,
            "timestamp": self.deadline,
            "checked": self.checked
        }

class Subject(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    subject = models.CharField(max_length=200)
    category = models.CharField(max_length=64, null=True)

    def serialize(self):
        return {
            "user": self.user,
            "subject": self.subject,
            "category": self.category
        }

class URL(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=200, blank=True, default=None)
    subject = models.CharField(max_length=200)
    links = models.URLField(max_length = 200, blank=True, default=None)

    def serialize(self):
        return {
            "subject": self.subject,
            "links": self.links,
            "name": self.name
        } 

class Notes(models.Model):
    objects = models.Manager()
    user =  user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    subject = models.CharField(max_length=200)
    note = models.CharField(max_length=200)

    def serialize(self):
        return {
            "user": self.user,
            "subject": self.subject,
            "note": self.note
        } 
    
