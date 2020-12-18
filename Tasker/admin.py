from django.contrib import admin
from .models import User, Tasks, Subject, URL, Notes

# Register your models here.
admin.site.register(User)
admin.site.register(Tasks)
admin.site.register(Subject)
admin.site.register(URL)
admin.site.register(Notes)
