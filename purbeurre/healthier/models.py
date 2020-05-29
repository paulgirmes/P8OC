from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


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
    def get_favorites(username):
        favorites = Food_item.objects.filter(favoris__username=username)
        if favorites.exists():
            return favorites
        else:
            return False
    @staticmethod
    def save_favorites(food_id, user):
        try:
            f=Food_item.objects.get(id=food_id)
            f.favoris.get(username=user)
            return {"result":"already existing", "status":False}                      
        except ObjectDoesNotExist:
            try:
                f.favoris.add(user)
                return {"result":"added", "status":True}
            except:
                return {"result":"unforeseen exception", "status":False}
        else:
            return {"result":"unforeseen exception", "status":False} 
        
        