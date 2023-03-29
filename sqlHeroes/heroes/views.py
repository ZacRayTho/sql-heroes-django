from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero, Power, Relationship_type, Relationship
from django.http import JsonResponse
import json 


def heroes(request):
    x = Hero.objects.all()
    html = ''
    for item in x:
        html += '<li> %s </li>'% item.name
    return HttpResponse("All Heroes: %s " % html)


def detailed_hero(request, hero_id):
    x = Hero.objects.get(pk=hero_id)
    y = Power.objects.filter(hero__name=x.name)
    z = Relationship.objects.filter(hero2__name=x.name) | Relationship.objects.filter(hero1__name=x.name)
    # y works but this is better practice probably
    print(x.powers.all())
    
    return HttpResponse("%s is the best hero, he has %s, and %s"% (x.name, y[0].name, z[0]))


def power(request, power):
    x = Hero.objects.filter(powers__name=power)
    list = [] 
    print(x)
    for dude in x:
        list.append(dude.name)

    return HttpResponse('%s has %s'% (list, power) )

def json(request):
    data = list(Hero.objects.values())
    return JsonResponse(data, safe=False)
