from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView

from .models import Wish

# Create your views here.


class WishList(ListView):
    model = Wish


class WishCreate(CreateView):
    model = Wish
    fields = '__all__'


class WishDelete(DeleteView):
    model = Wish
    success_url = '/'