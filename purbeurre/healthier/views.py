from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import FoodQuery
from django.contrib.auth import logout
from django.urls import reverse



def home(request):
    form = FoodQuery(auto_id="recherche_%s")
    form1 = FoodQuery(auto_id="recherche_2_%s")
    context={'form': form, 'form1': form1}
    if not request.user.is_authenticated:
        context.update({"logged":"False"})
    else:
        context.update({"logged":"True"})
    return render(request, "healthier/_index.html", context)

@login_required(login_url="healthier:login")
def myaccount(request):
    form1 = FoodQuery(auto_id="recherche_2_%s")
    context = {
        "logged": "True",
        'form1': form1,
        "user_name": "Paul",
        "user_mail": "paul@qqqq.fr",
    }
    return render(request, "healthier/_user_page.html", context)

@login_required(login_url="healthier:login")
def myfoods(request):
    form1 = FoodQuery(auto_id="recherche_2_%s")
    message ={
        'form1': form1,
        "food_items":["item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3"]}
    return render(request, "healthier/_my_saved_foods.html", message)


def login(request):
    if not request.user.is_authenticated:
        form1 = FoodQuery(auto_id="recherche_2_%s")
        message ={
        'form1': form1,
        }
        return render(request, "healthier/_login_signin.html", message)
    else:
        logout(request)
        return redirect(reverse("healthier:home"))

def results(request):
    form1 = FoodQuery(auto_id="recherche_2_%s")
    query = request.GET['fooditem']
    message = {
        'form1': form1,
        "food_items":[{"id":"1"}, {"id":"1"}, {"id":"1"},{"id":"1"}, {"id":"1"}, {"id":"1"}, {"id":"1"}, {"id":"1"},],
        "img_url":"https://static.openfoodfacts.org/images/products/316/544/000/8935/front_fr.18.full.jpg",
        "searched": query
            }
    return render(request, "healthier/_results.html", message)

def contact(request):
    form1 = FoodQuery(auto_id="recherche_2_%s")
    message = {
        'form1': form1,
        }
    return render(request, "healthier/_contact.html", message)

def fooditem(request):
    form1 = FoodQuery(auto_id="recherche_2_%s")
    message = {
        'form1': form1,
        "name": "pates",
        "nutriscore": "a",
        "energy_kcal_100gr":"250",
        "img_url":"https://static.openfoodfacts.org/images/products/316/544/000/8935/front_fr.18.full.jpg",
        "openfoodfacts_url":"https://fr.openfoodfacts.org/produit/3165440008621/cereales-gourmandes-tipiak"
    }
    return render(request, "healthier/_food_item.html", message)

def general_conditions(request):
    form1 = FoodQuery(auto_id="recherche_2_%s")
    message = {
        'form1': form1,
        }
    return render(request, "healthier/_legal_content.html", message)