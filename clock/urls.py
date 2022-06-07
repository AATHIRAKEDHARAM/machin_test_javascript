from . import views
from django.urls import path

urlpatterns = [
    path('',views.clock,name="clock"),
    path('todo',views.todo,name="todo"),
]