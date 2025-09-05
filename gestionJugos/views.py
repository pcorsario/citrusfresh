from django.shortcuts import render

# Instanciar vistas genericas
# from django.views.generic import ListView, DetailView
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Jugos
# from django.urls import reverse
# from django.contrib import messages
# from django.contrib.messages.views import SuccessMessageMixin
# from django import forms

# class ListarJugos(ListView):
#     model = Jugos

def dashboard(request):
    return render(request, 'jugos/dashboard.html')

def jugos(request):
    jugos = Jugos.objects.all()
    return render(request, 'jugos/index.html', {'jugos': jugos})