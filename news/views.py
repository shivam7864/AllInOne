from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime

# Create your views here.

def index(request):

    api=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=c1f878090ef6465d889a58949dcbfbe8')

    res=api.json()
    
    context={'res':res}
    return render (request,'news/index.html',context)



def globalnews(request):

    api=requests.get('https://newsapi.org/v2/everything?q=top-headlines&apiKey=c1f878090ef6465d889a58949dcbfbe8')

    res=api.json()
    
    context={'res':res}
    return render (request,'news/globalnews.html',context)


def business(request):

    api=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c1f878090ef6465d889a58949dcbfbe8')

    res=api.json()
    
    context={'res':res}
    return render (request,'news/business.html',context)


def entertainment(request):

    api=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=c1f878090ef6465d889a58949dcbfbe8')

    res=api.json()
    
    context={'res':res}
    return render (request,'news/entertainment.html',context)


def bitcoin(request):

    api=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=bitcoin&apiKey=c1f878090ef6465d889a58949dcbfbe8')

    res=api.json()
    
    context={'res':res}
    return render (request,'news/bitcoin.html',context)
    
def sports(request):

    api=requests.get('https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=c1f878090ef6465d889a58949dcbfbe8')

    res=api.json()
    
    context={'res':res}
    return render (request,'news/sports.html',context)





