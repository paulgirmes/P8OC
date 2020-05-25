from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned


class Store(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Food_item(models.Model):
    open_food_facts_url = models.URLField(max_length=400)
    name = models.CharField(max_length=200)
    energy_100g = models.CharField(max_length=20)
    nutri_score_fr = models.CharField(
        max_length=1, choices=[("a", "a"), ("b", "b"), ("c", "c"), ("d", "d")]
    )
    nova_grade = models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])
    image_url = models.URLField(max_length=400)
    id_open_food_facts = models.BigIntegerField(unique=True)
    stores = models.ManyToManyField(Store)
    brands = models.ManyToManyField(Brand)
    categories = models.ManyToManyField(Category)
    favoris = models.ManyToManyField(User)

    def __str__(self):
        return self.name
    
    @staticmethod
    def search(food_name):
        try:
            f = Food_item.objects.filter(name__icontains=food_name)
            return f
        except:
            return False
       

    @staticmethod
    def replace(food_name):
        try:
            food_item=Food_item.search(food_name)
        except MultipleObjectsReturned:
            raise
        if food_item != False:
            categories = food_item.categories.all()[:4]
            replacement = Food_item.objects.filter(
                    categories__name__icontains=categories[0],
                    nova_grade__lt=food_item.nova_grade, 
                    nutri_score_fr__lt=food_item.nutri_score_fr,
                    ).filter(categories__name__icontains=categories[1]).filter(categories__name__icontains=categories[2]).filter(categories__name__icontains=categories[3])
            if replacement.exists():
                return replacement
        else:
            raise ValueError("Il n'existe pas d'aliment '"+food_name+"' dans la base de données")
