from django.shortcuts import render
from django.http import HttpResponse
import requests
import tutorme.apiutils as sisapi
import urllib.parse


# Create your views here.
def index(request):
    
    classList = []
    searchParams = ''
    data = request.GET.get('data')
    if request.method == 'GET' and 'search' in request.GET:
        searchParams = request.GET.get('search', '')
        classList = sisapi.search_matcher(searchParams)

    if request.method == 'GET' and 'data' in request.GET:
        data = urllib.parse.unquote(request.GET.get('data', ''))
        
    context = {'classList': classList, 'search':searchParams, 'requestedClass':data}

    return render(request, 'tutorme/index.html', context)