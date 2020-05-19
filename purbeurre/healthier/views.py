from django.shortcuts import render
from django.http import HttpResponse

from .forms import FoodQuery

def home(request):
    form = FoodQuery(auto_id="recherche_%s")
    form1 = FoodQuery(auto_id="recherche_2%s")
    context={'form': form, 'form1': form1}
    return render(request, "healthier/_index.html", context)

def myaccount(request):
    form1 = FoodQuery(auto_id="recherche_2%s")
    message= {
        'form1': form1,
        "user_name": "Paul",
        "user_mail": "paul@qqqq.fr",
    }
    return render(request, "healthier/_user_page.html", message)

def myfoods(request):
    form1 = FoodQuery(auto_id="recherche_2%s")
    message ={
        'form1': form1,
        "food_items":["item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3"]}
    return render(request, "healthier/_my_saved_foods.html", message)

def logout(request):
    return HttpResponse('logout')

def results(request):
    form1 = FoodQuery(auto_id="recherche_2%s")
    query = request.GET['fooditem']
    message = {
        'form1': form1,
        "food_items":[{"id":"1"}, {"id":"1"}, {"id":"1"},{"id":"1"}, {"id":"1"}, {"id":"1"}, {"id":"1"}, {"id":"1"},],
        "img_url":"https://static.openfoodfacts.org/images/products/316/544/000/8935/front_fr.18.full.jpg",
        "searched": query
            }
    return render(request, "healthier/_results.html", message)

def contact(request):
    form1 = FoodQuery(auto_id="recherche_2%s")
    message = {
        'form1': form1,
        }
    return render(request, "healthier/_contact.html", message)

def fooditem(request):
    form1 = FoodQuery(auto_id="recherche_2%s")
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
    form1 = FoodQuery(auto_id="recherche_2%s")
    message = {
        'form1': form1,
        }
    return render(request, "healthier/_legal_content.html", message)