from django.shortcuts import render, redirect
from .models import UserModel, Order
from datetime import datetime
from django.db.models import Avg, Sum, Min, Max
from .forms import *


def index(request):
    st = '-name'
    people = UserModel.objects.all()
    chel = UserModel.objects.aggregate(Min('age'))
    return render(request, 'app/index.html', context={'people': people})


def orders(request):
    createOrders()
    orders = Order.objects.filter(datetime__month__gte=6)
    return render(request, 'app/orders.html', context={'orders': orders})


def createOrders():
    if Order.objects.count() < 5:
        Order.objects.create(datetime=datetime(2000, 6, 23, 12, 23, 55))
        Order.objects.create(datetime=datetime(2020, 2, 12, 12, 23, 55))
        Order.objects.create(datetime=datetime(2023, 3, 23, 12, 23, 55))
        Order.objects.create(datetime=datetime(2024, 7, 23, 12, 23, 55))


def create(request):
    if request.method == "POST":
        form = AddMen(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            UserModel.objects.create(name=name, age=age)
            return redirect('home')
    form = AddMen()
    return render(request, 'app/create.html', context={'form': form})


def update(request, id):
    try:
        men = UserModel.objects.get(id=id)
        if request.method == "POST":
            men.name = request.POST.get('name')
            men.age = request.POST.get('age')
            men.save()
            return redirect('home')
        else:


            return render(request, 'app/update.html', context={'men': men})

    except:
        return redirect('create')

def delete(request, id):
    try:
        men = UserModel.objects.get(id=id)
        men.delete()
        return redirect('home')
    except:
        return redirect('home')

def user(request, id):
    try:
        men = UserModel.objects.get(id=id)
        return render(request, 'app/user.html', context={'men': men})
    except:
        return redirect('home')
