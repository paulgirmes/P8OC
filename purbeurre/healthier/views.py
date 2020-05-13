from django.shortcuts import render
from django.http import HttpResponse

from .forms import FoodQuery

def home(request):
    form = FoodQuery()
    context={'form': form}
    return render(request, "healthier/_index.html", context)

def myaccount(request):
    return HttpResponse('myaccount')

def myfoods(request):
    return HttpResponse('myfoods')

def logout(request):
    return HttpResponse('logout')

def results(request):
    obj = str(request.GET)
    query = request.GET['fooditem']
    message = "propriété GET : {} et requête : {}".format(obj, query)
    return HttpResponse(message)

def contact(request):
    return HttpResponse("contacts")


def general_conditions(resquest):
    return HttpResponse("legal")