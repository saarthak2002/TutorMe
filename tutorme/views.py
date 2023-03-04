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
    tutorList = []
    if request.method == 'GET' and 'search' in request.GET:
        searchParams = request.GET.get('search', '')
        classList = sisapi.search_matcher(searchParams)

    if request.method == 'GET' and 'data' in request.GET:
        data = urllib.parse.unquote(request.GET.get('data', ''))
        default_bio = 'Hello, I am a tutor for {}. Nice to meet you!'.format(data)
        
        # TESTER DATA
        tutorList = [
            {'name':'John Doe', 'class': data, 'Bio': default_bio},
            {'name':'Jane Doe', 'class': data, 'Bio': default_bio},
            {'name':'Sarah Myers', 'class': data, 'Bio': default_bio},
            {'name':'The Rock', 'class': data, 'Bio': default_bio},
            {'name':'Forrest Gump', 'class': data, 'Bio': default_bio},
            {'name':'Robert Sun', 'class': data, 'Bio': default_bio},
            {'name':'Vaughn Scott', 'class': data, 'Bio': default_bio},
            {'name':'Michael Kim', 'class': data, 'Bio': default_bio},
            {'name':'Dorothy Parker', 'class': data, 'Bio': default_bio}
        ]
        
    context = {'classList': classList, 'search':searchParams, 'requestedClass':data, 'tutorList':tutorList}

    return render(request, 'tutorme/index.html', context)