from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("archive", views.archive, name="archive"),
    path("subjects", views.subjects, name="subjects"),
    path("subject/<str:subject>", views.subject, name="subject"),

    #API paths
    path("add", views.add, name="add"),
    path("check/<int:task_id>", views.check, name="check"),
    path("delete/<int:task_id>", views.delete, name="delete"),
    path("subject/<str:subject>/delete/<int:link_id>", views.delete_link, name="delete_link"),
    path("subject/<str:subject>/edit/<int:note_id>", views.edit_note, name="edit_note"),
    path("<str:category>", views.filter, name="filter")


]