from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import requests
from datetime import datetime

# Create your views here.

def index(request):

    api=requests.get('https://api.covid19api.com/summary')

    res=api.json()
    
    context={'res':res}
    return render (request,'covid_tracker/index.html',context)


def countrywise(request):
    api=requests.get('https://api.covid19api.com/summary')

    res=api.json()
    
    context={'res':res}
    return render (request,'covid_tracker/countrywise.html',context)

def search(request):
    api=requests.get('https://api.covid19api.com/summary')
    res=api.json()
    query=None
    timeStamp=datetime.now()
    result=res['Countries']
    if request.method=='GET':
        query=request.GET.get('query').lower()

    result=res['Countries']
    for c in result:
        if c['Country'].lower()==query:
            params={
                'query':query.upper(),
                'nc':c['NewConfirmed'],
                'tc':c['TotalConfirmed'],
                'nd':c['NewDeaths'],
                'td':c['TotalDeaths'],
                'ts':timeStamp
            }
            return render(request,'covid_tracker/search.html',params)
    context={'msg':'Sorry,you asked for the country which does not exist'}
    return render(request,'covid_tracker/search.html',context)

       
   


