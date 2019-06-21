from django.db import models
from django.shortcuts import render
from django.urls import reverse

# Create your models here.


class Wish(models.Model):
    description = models.TextField(max_length=500)

    def get_absolute_url(self):
        return reverse('wish_list')
