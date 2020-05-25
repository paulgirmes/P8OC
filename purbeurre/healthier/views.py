from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.db.utils import IntegrityError

from .forms import FoodQuery, Signin, Login
from django.contrib.auth import logout
from django.urls import reverse



def home(request):
    form = FoodQuery(auto_id="recherche_%s")
    form1 = FoodQuery(auto_id="recherche_2_%s")
    context={'form': form, 'form1': form1}
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
        sign_form = Signin(auto_id="signin%s")
        log_form = Login(auto_id="login%s")
        message ={
        'form1': form1, 'sign_form': sign_form, "log_form": log_form,
        }
        if request.method == "POST":
            sign_form = Signin(request=request, data=request.POST, auto_id="signin%s")
            try:
                e = sign_form.save()
                if e == True:
                    return redirect(reverse("healthier:myaccount"))
                else:
                    message.update({"sign_form":sign_form, "modaltoshow":"SigninModal"})
            except Exception as e:
                return HttpResponse(e)
        elif "username" in request.GET:
            log_form = Login(request, data=request.GET, auto_id="login%s")
            try:
                log_form.log_user()
                return redirect(reverse("healthier:myaccount"))
            except:
                message.update({"modaltoshow":"LoginModal", "log_form":log_form})

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