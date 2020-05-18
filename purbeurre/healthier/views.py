from django.shortcuts import render
from django.http import HttpResponse

from .forms import FoodQuery

def home(request):
    form = FoodQuery()
    context={'form': form}
    return render(request, "healthier/_index.html", context)

def myaccount(request):
    message= {
        "user_name": "Paul",
        "user_mail": "paul@qqqq.fr"
    }
    return render(request, "healthier/_user_page.html", message)

def myfoods(request):
    message ={"food_items":["item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3","item1", "item2", "item3"]}
    return render(request, "healthier/_my_saved_foods.html", message)

def logout(request):
    return HttpResponse('logout')

def results(request):
    query = request.GET['fooditem']
    message = {"food_items":[{"id":"1"}, {"id":"1"}, {"id":"1"},{"id":"1"}, {"id":"1"}, {"id":"1"}, {"id":"1"}, {"id":"1"},],
                "img_url":"https://static.openfoodfacts.org/images/products/316/544/000/8935/front_fr.18.full.jpg",
                "searched": query
                }
    return render(request, "healthier/_results.html", message)

def contact(request):
    return render(request, "healthier/_contact.html")

def fooditem(request):
    message = {
        "name": "pates",
        "nutriscore": "a",
        "energy_kcal_100gr":"250",
        "img_url":"https://static.openfoodfacts.org/images/products/316/544/000/8935/front_fr.18.full.jpg",
        "openfoodfacts_url":"https://fr.openfoodfacts.org/produit/3165440008621/cereales-gourmandes-tipiak"
    }
    return render(request, "healthier/_food_item.html", message)

def general_conditions(request):
    return render(request, "healthier/_legal_content.html")