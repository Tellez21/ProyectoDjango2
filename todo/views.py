from django.shortcuts import render, redirect
from .models import tarea
from .forms import tareaform
# Create your views here.
def home(request):
    tareas=tarea.objects.all()
    context={'tareas':tareas}
    return render(request,'todo/home.html',context)

def agregar (request):
    if request.method =="POST":
        form = tareaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = tareaform()
            
        context = {'form' : form}
        return render(request, 'todo/agregar.html', context)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            