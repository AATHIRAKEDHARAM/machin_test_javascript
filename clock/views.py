from django.shortcuts import render

# Create your views here.

def clock(request):
    return render(request,"clock/clock.html")
def todo(request):
    return render(request,"clock/todo.html")
