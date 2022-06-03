from django.shortcuts import render, redirect
from .models import Category, Drink

def make_form(request):
    if request.method == 'POST':

        return ''
    elif request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'drink.html', {'categories':categories})