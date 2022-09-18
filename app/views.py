from django.shortcuts import render,redirect
from .models import Carro
from app.forms import CarrosForm

# Create your views here.
def home(request):
    carros = Carro.objects.all()
    return render(request,'index.html', {'carros' : carros})

def form(request):
    data = {}
    data["form"] = CarrosForm()
    return render(request, 'form.html', data)

def create(request):
    form = CarrosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request,pk):
    carros = Carro.objects.get(pk=pk)
    return render(request, 'view.html' , {'carros': carros})

def edit(request,pk):
    data = {}
    data['carros'] =  Carro.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['carros'])
    return render(request, 'form.html', data)

def update(request,pk):
    data = {}
    data['carros'] = Carro.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['carros'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request,pk):
    carros = Carro.objects.get(pk=pk)
    carros.delete()
    return redirect('home')