from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero, Power, Relationship_type, Relationship

def heroes(request):
    x = Hero.objects.all()
    list = []
    for item in x:
        list.append(item.name)
    # print(list)
    return HttpResponse("All Heroes: %s " % list)
# Create your views here.

def detailed_hero(request, hero_id):
    x = Hero.objects.get(pk=hero_id)
    return HttpResponse("%s is the best hero"% x)
