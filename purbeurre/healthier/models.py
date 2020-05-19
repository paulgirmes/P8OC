from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        print(self.name)

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __repr__(self):
        print(self.name)

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __repr__(self):
        print(self.name)


class Food_item(models.Model):
    open_food_facts_url = models.URLField(max_length=400, unique=True)
    name = models.CharField(max_length=200, unique=True)
    energy_kcal_100gr = models.BigIntegerField()
    nutri_score_fr = models.CharField(max_length=1, choices=[("a", "a"), ("b","b"), ("c","c"), ("d","d")])
    nova_grade = models.IntegerField(choices=[(1,1), (2,2), (3,3),(4,4)])
    image_url = models.URLField(max_length=400, unique=True)
    id_open_food_facts = models.BigIntegerField(unique=True)
    stores = models.ManyToManyField(Store)
    Brands = models.ManyToManyField(Brand)
    categories = models.ManyToManyField(Category)
    favoris = models.ManyToManyField(User)


    def __repr__(self):
        print(self.name + " / " + self.open_food_facts_url)

