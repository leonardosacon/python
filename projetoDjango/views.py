from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .models import Zona

def index(request):
    lista_zona = Zona.objects.order_by('id')
    context = {'lista_zona': lista_zona}
    return render(request, '../static/../templates/index.html', context)
