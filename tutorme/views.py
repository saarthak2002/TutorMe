from django.shortcuts import render
import tutorme.apiutils as sisapi
import urllib.parse
from .models import Tutor, AppUser, Request, Ratings

def index(request):
    
    classList = []
    searchParams = ''
    data = request.GET.get('data')
    tutorList = []

    if request.method == 'POST':
        from_student = request.POST.get('from')
        to_tutor = request.POST.get('to')
        course = request.POST.get('course')
        user_student = AppUser.objects.filter(user__username__contains = from_student).first()
        user_tutor = AppUser.objects.filter(user__username__contains = to_tutor).first()

        new_request , created = Request.objects.get_or_create(
            from_student = user_student,
            to_tutor = user_tutor,
            course = course,
            status = 1
        )
        new_request.save()

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

def student_requests_view(request):
    request_list = []

    if request.method == 'POST':
        remove_from_student = request.POST.get('from') #username
        remove_to_tutor = request.POST.get('to')
        remove_course = request.POST.get('course')
        user_student = AppUser.objects.filter(user__username__contains = remove_from_student).first()
        user_tutor = AppUser.objects.filter(user__username__contains = remove_to_tutor).first()
        
        remove_query = Request.objects.filter(
            from_student = user_student,
            to_tutor = user_tutor,
            course = remove_course
        ).delete()

    username = request.user.username
    query_result = Request.objects.filter(from_student__user__username__contains = username)
    for item in query_result:
        to_tutor = item.to_tutor.user.username
        tutor_name = item.to_tutor.user.first_name + ' ' + item.to_tutor.user.last_name
        tutor_email = item.to_tutor.user.email
        course = item.course
        time = item.created_timestamp
        str_time = time.strftime("sent on %m-%d-%Y at %H:%M:%S")
        status = 'Pending' if item.status == 1 else 'Accepted' if item.status == 2 else 'Declined'
        request_list.append({'to_tutor':to_tutor, 'tutor_name':tutor_name, 'course':course, 'status':status, 'tutor_email':tutor_email, 'time':str_time})
    
    context = {'request_list': request_list}
    return render(request, 'tutorme/studentRequestsView.html', context)

def tutor_requests_view(request):
    request_list = []

    if request.method == 'POST':
        change_status_request_type = request.POST.get('request_type')
        change_status_from_student = request.POST.get('from')
        change_status_to_tutor = request.POST.get('to')
        change_status_course = request.POST.get('course')
        print('from:{} to: {} for: {} change to: {}'.format(change_status_from_student,change_status_to_tutor,change_status_course,change_status_request_type))
        # change DB data here

    context = {'request_list':request_list}
    return render(request, 'tutorme/tutorRequestsView.html', context)

def tutor_my_classes_view(request):

    course_list = []
    curr_user = request.user.username
    current_tutor = AppUser.objects.filter(user__username__contains = curr_user).first()

    # Implement Remove POST
    if request.method == 'POST':
        curr_user = request.user.username
        current_tutor = AppUser.objects.filter(user__username__contains = curr_user).first()
        remove_course = request.POST.get('course')
        
        tutor_to_remove = Tutor.objects.filter(
            user = current_tutor,
            course = remove_course
        ).delete()

    course_query = Tutor.objects.filter(
        user = current_tutor
    )

    for item in course_query:
        course = item.course
        course_list.append(course)

    context = {'course_list' : course_list}
    return render(request, 'tutorme/tutorMyClassesView.html', context)

def tutor_add_classes_view(request):
    classList = []
    searchParams = ''

    if request.method == 'POST':
        course = request.POST.get('course')
        curr_user = request.user.username
        current_tutor = AppUser.objects.filter(user__username__contains = curr_user).first()
        
        new_tutor, created = Tutor.objects.get_or_create(
            user = current_tutor,
            course = course
        )
        new_tutor.save()

    if request.method == 'GET' and 'search' in request.GET:
        searchParams = request.GET.get('search', '')
        classList = sisapi.search_matcher(searchParams)

    context = {'classList': classList, 'search':searchParams}
    return render(request, 'tutorme/tutorAddClassesView.html', context)

def tutor_profile_view(request):
    classes_list = []
    ratings_list = []
    tutor_user_id = request.user.id
    tutor_app_id = AppUser.objects.filter(user_id__id = tutor_user_id).values('id')[0]['id']
    rating_query_result = Ratings.objects.filter(tutor_who_was_rated__id = tutor_app_id)
    classes_query_result = Tutor.objects.filter(user_id__id = tutor_app_id)
    for rating in rating_query_result:
        from_student = rating.student_who_rated.user.username
        student_name = rating.student_who_rated.user.first_name + ' ' + rating.student_who_rated.user.last_name
        student_email = rating.student_who_rated.user.email
        given_rating = rating.rating
        review = rating.review
        ratings_list.append({'from_student':from_student, 'student_name':student_name, 'rating':given_rating, 'review': review, 'student_email':student_email})
    for class_tutored in classes_query_result:
        course = class_tutored.course
        classes_list.append({'course': course})
    context = {'ratings_list': ratings_list, 'classes_list': classes_list}

    return render(request, 'tutorme/tutorProfile.html', context)
