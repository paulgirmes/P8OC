import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseServerError, Http404, HttpResponseServerError, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.db.utils import IntegrityError

from .forms import FoodQuery, Signin, Login
from django.contrib.auth import logout
from django.urls import reverse
from .models import Food_item


def home(request):
    form = FoodQuery(auto_id="form")
    form1 = FoodQuery(auto_id="form1")
    context={'form': form, 'form1': form1}
    return render(request, "healthier/_index.html", context)

@login_required(login_url="healthier:login")
def myaccount(request):
    form1 = FoodQuery(auto_id="form1")
    context = {
        'form1': form1,
        "user_name": request.user.first_name,
        "user_mail": request.user.email,
    }
    return render(request, "healthier/_user_page.html", context)

@login_required(login_url="healthier:login")
def myfoods(request):
    form1 = FoodQuery(auto_id="form1")
    message ={
        'form1': form1,
        "food_items": "",
        }
    favorites = Food_item.get_favorites(request.user.username)
    message["food_items"]=favorites
    return render(request, "healthier/_my_saved_foods.html", message)


def login(request):
    form1 = FoodQuery(auto_id="form1")
    if not request.user.is_authenticated:
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
            except:
                return HttpResponseServerError
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
    form1 = FoodQuery(auto_id="form1")
    message = {
        'form1': form1,
        "food_items":"",
        "searched": "",
            }
    if "form" in request.GET:
        form = FoodQuery(data=request.GET, auto_id="form", align="")
        results = form.get_searched_food_Item()
        if  results == 1:
            message["food_items"]=form.replacement_foods
            message["searched"]=form.food_item
            
        elif results > 1:
            message.update({"form": form})
            message["searched"]=form.food_item
            
        elif not results:
            message.update({"form": form})
            
                
    elif "form1" in request.GET:
        form1 = FoodQuery(data=request.GET, auto_id="form", align="")
        if form1.get_searched_food_Item() == 1:
            message["food_items"]=form1.replacement_foods
            message["searched"]=form1.food_item
           
        else:
            message.update({"form": form1})
            
    elif request.method == "POST":
        result = Food_item.save_favorites(request.POST["value"], request.user)
        return HttpResponse(json.dumps(result))



    return render(request, "healthier/_results.html", message)

def contact(request):
    form1=FoodQuery(auto_id="form1")
    message = {
        'form1': form1,
        }
    return render(request, "healthier/_contact.html", message)

def fooditem(request):
    form1 = FoodQuery(auto_id="form1")
    message = {
        "form1":form1,
        "food_item":"",
    }
    message["food_item"]= Food_item.objects.get(id=request.GET["food_id"])
    return render(request, "healthier/_food_item.html", message)

def general_conditions(request):
    form1 = FoodQuery(auto_id="form1")
    message = {
        'form1': form1,
        }
    return render(request, "healthier/_legal_content.html", message)