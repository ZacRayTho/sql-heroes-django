from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    bio = models.CharField(max_length=300)
    powers = models.ManyToManyField('Power')

    def __str__(self):
        return self.name
    
class Power(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Relationship_type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Relationship(models.Model):
    hero1 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero1')
    hero2 = models.ForeignKey(Hero, on_delete=models.PROTECT, related_name='hero2')
    relationship = models.ForeignKey(Relationship_type, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.hero1}, and {self.hero2} are {self.relationship}s'

# Create your models here.
