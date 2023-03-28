from django.contrib import admin

from .models import Hero, Power, Relationship, Relationship_type

admin.site.register(Hero)
admin.site.register(Power)
admin.site.register(Relationship)
admin.site.register(Relationship_type)
# Register your models here.
