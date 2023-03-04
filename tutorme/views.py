from django.shortcuts import render
from django.http import HttpResponse
import requests
import tutorme.apiutils as sisapi


# Create your views here.
def index(request):
    
    classList = []
    searchParams = ''
    if request.method == 'GET' and 'search' in request.GET:
        searchParams = request.GET.get('search', '')
        classList = sisapi.search_matcher(searchParams)
        
    context = {'classList': classList, 'search':searchParams}

    return render(request, 'tutorme/index.html', context)