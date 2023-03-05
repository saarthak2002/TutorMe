from django.shortcuts import render
import tutorme.apiutils as sisapi
import urllib.parse
from .models import Tutor

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
        query_result = Tutor.objects.filter(course__contains = data)
        for tutor in query_result:
            name = tutor.user.user.first_name + ' ' + tutor.user.user.last_name
            username = tutor.user.user.username
            email = tutor.user.user.email
            tutorList.append({'name':name, 'class': data, 'Bio': default_bio, 'username': username, 'email': email})
        
    context = {'classList': classList, 'search':searchParams, 'requestedClass':data, 'tutorList':tutorList}

    return render(request, 'tutorme/index.html', context)