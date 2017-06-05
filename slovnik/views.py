from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("index")


def learn(request):
    return HttpResponse("seznam kategorii")


def category(request, category):
    return HttpResponse("detail kategorie: "+category)


def detail(request, category, word_id):
    return HttpResponse("slovo c. "+word_id+" v kategorii "+ category)
