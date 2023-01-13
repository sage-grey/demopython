from django.urls import path

from . import views

urlpatterns = [
    path('',views.Tasks,name="Tasks"),
    path('delete/<int:taskid>/',views.delete,name="delete"),
    path('edit/<int:id>/',views.update,name="update"),
    ]