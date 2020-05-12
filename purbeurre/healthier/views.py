from django.shortcuts import render
from  django.http import HttpResponse

def home(request):
    return render(request, "purbeurre\\base.html")

def myaccount(request):
    return HttpResponse('myaccount')

def myfoods(request):
    return HttpResponse('myfoods')

def logout(request):
    return HttpResponse('logout')

def results(request):
    obj = str(request.GET)
    query = request.GET['query']
    message = "propriété GET : {} et requête : {}".format(obj, query)
    return HttpResponse(message)
