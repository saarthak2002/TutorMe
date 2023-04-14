from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
import tutorme.apiutils as sisapi
import urllib.parse
from .models import Tutor, AppUser, Request, Ratings, TutorTimes
from datetime import datetime

# check what kind of user is logged in, if any
def check_logged_in(request):
    if request.user.is_authenticated:
        return request.user.appuser.user_type
    else:
        return 0

# student view class search page (Search)
def index(request):
    
    classList = []
    searchParams = ''
    data = request.GET.get('data')
    tutorList = []
    date = ""
    time = ""
    request_list = []
    # handle clicking "Request Help" button after search and display tutor list, adds new Request to database
    if request.method == 'POST':
        from_student = request.POST.get('from')
        to_tutor = request.POST.get('to')
        course = request.POST.get('course')
        date_requested = request.POST.get('date')
        start_time_requested = request.POST.get('start')
        end_time_requested = request.POST.get('end')
        user_student = AppUser.objects.filter(user__username__contains = from_student).first()
        user_tutor = AppUser.objects.filter(user__username__contains = to_tutor).first()
        # TO FIX: CHECK IF REQUEST WITH PARAMETERS ALREADY EXISTS

        new_request , created = Request.objects.get_or_create(
            from_student = user_student,
            to_tutor = user_tutor,
            course = course,
            status = 1,
            date_requested = date_requested,
            start_time_requested = start_time_requested,
            end_time_requested = end_time_requested
        )
        new_request.save()
    # displays list of classes in table on clicking "Search" button after entering search parameters in search bar
    # queries SIS API for list of classes based on parameters
    if request.method == 'GET' and 'search' in request.GET:
        searchParams = request.GET.get('search', '')
        classList = sisapi.search_matcher(searchParams)

    # displays list of tutor cards on clicking "Request" button for a course in the search results table
    if request.method == 'GET' and 'data' in request.GET:
        data = urllib.parse.unquote(request.GET.get('data', ''))
        time = urllib.parse.unquote(request.GET.get('time', ''))
        date = urllib.parse.unquote(request.GET.get('date', ''))

        if date:
            format_date = datetime.strptime(date, "%Y-%m-%d")
            day_of_week = format_date.strftime("%A")
            
        #THIS IS WHERE IT HAPPENS
        default_bio = 'Hello, I am a tutor for {}. Nice to meet you!'.format(data)
        query_result = Tutor.objects.filter(course__contains = data)
        for tutor in query_result:
            available_at_requested_time = False
            tutor_id = tutor.user.id
            entry_exists = TutorTimes.objects.filter(user_id__id = tutor_id).exists()
            hourly_rate = 10.00
            if entry_exists:
                tutor_times_query = TutorTimes.objects.get(user_id__id = tutor_id)
                available_times = tutor_times_query.available_times
                hourly_rate = tutor_times_query.hourly_rate
                if available_times:
                    day_requested_times = available_times[day_of_week]
                    if time in day_requested_times:
                        available_at_requested_time = True
                if available_at_requested_time is True:
                    name = tutor.user.user.first_name + ' ' + tutor.user.user.last_name
                    username = tutor.user.user.username
                    email = tutor.user.user.email
                    tutorList.append({'name':name, 'class': data, 'Bio': default_bio, 'username': username, 'email': email, 'hourly_rate':hourly_rate})
    
    test_if_tutor = AppUser.objects.filter(user__username__contains = request.user.username).first()
    
    if test_if_tutor.user_type == 2:
        username = request.user.username
        query_result = Request.objects.filter(to_tutor__user__username__contains = username)

        for item in query_result:
            from_student = item.from_student.user.username
            student_name = item.from_student.user.first_name + ' ' + item.from_student.user.last_name
            student_email = item.from_student.user.email
            course = item.course
            time = item.created_timestamp
            str_time = time.strftime("sent on %m-%d-%Y at %H:%M:%S")
            status = 'Pending' if item.status == 1 else 'Accepted' if item.status == 2 else 'Declined'
            date = item.date_requested
            start = item.start_time_requested
            end = item.end_time_requested
            # Show the tutor the accepted sessions they have scheduled in the next 7 days
            if(item.is_upcoming() and item.status == 2):
                request_list.append({'from_student':from_student, 'student_name':student_name, 'course':course, 'status':status, 'student_email':student_email, 'time':str_time, 'date': date, 'start': start, 'end':end})
    
    context = {'classList': classList, 'search':searchParams, 'requestedClass':data, 'tutorList':tutorList, 'date_requested':date, 'time_requested': time, 'request_list':request_list}
    
    return render(request, 'tutorme/index.html', context)

# student view requests page (My Requests)
def student_requests_view(request):
    if not check_logged_in(request):
        return render(request, 'tutorme/index.html', None)

    request_list = []

    # handle clicking "Remove" button on a card in the My Requests page in the Student View, removes Request from database
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

    # queries database for list of all Requests the current student has made, 
    # displaying all of them as cards in the My Requests view in the Student View
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
        date = item.date_requested
        start = item.start_time_requested
        end = item.end_time_requested
        request_list.append({'to_tutor':to_tutor, 'tutor_name':tutor_name, 'course':course, 'status':status, 'tutor_email':tutor_email, 'time':str_time, 'date':date, 'start': start, 'end': end})
    
    context = {'request_list': request_list}
    return render(request, 'tutorme/studentRequestsView.html', context)

# tutor view requests page (My Requests)
def tutor_requests_view(request):
    if not check_logged_in(request):
        return render(request, 'tutorme/index.html', None)

    request_list = []

    # handles clicking "Accept" or "Reject" button on a card in the My Requests page in the Tutor View,
    # changes the status of an existing Request in the database to Accepted or Declined- initially Pending
    if request.method == 'POST':
        change_status_request_type = request.POST.get('request_type')
        change_status_from_student = request.POST.get('from')
        change_status_to_tutor = request.POST.get('to')
        change_status_course = request.POST.get('course')
        start_time_requested = request.POST.get('start_time_requested')
        end_time_requested = request.POST.get('end_time_requested')
        date_requested = request.POST.get('date_requested')
        user_student = AppUser.objects.filter(user__username__contains = change_status_from_student).first()
        user_tutor = AppUser.objects.filter(user__username__contains = change_status_to_tutor).first()
        tutor_user_id = request.user.id
        tutor_app_id = AppUser.objects.filter(user_id__id = tutor_user_id).values('id')[0]['id']
        all_requests_to_tutor = Request.objects.filter(to_tutor_id__id = tutor_app_id)
        scheduling_conflict = False
        


        request_to_change = Request.objects.filter(
            from_student = user_student,
            to_tutor = user_tutor,
            course = change_status_course
        ).first()

        if change_status_request_type == 'accept':
            # for existing_request in all_requests_to_tutor:
            #     if existing_request.date_requested == date_requested:
            #         print('date conflict')
            #         conflict_query = Q(start_time_requested__range=(start_time_requested, end_time_requested)) | \
            #         Q(end_time_requested__range=(start_time_requested, end_time_requested)) | \
            #         Q(start_time_requested__lte=request.start_time_requested, end_time_requested__gte=request.end_time_requested)
            print('accepting here')
            request_to_change.status = 2
            request_to_change.save()
        elif change_status_request_type == 'reject':
            request_to_change.status = 3
            request_to_change.save()

    # queries database for list of all Requests the current tutor has received, 
    # displaying all of them as cards in the My Requests view in the Tutor View
    username = request.user.username
    query_result = Request.objects.filter(to_tutor__user__username__contains = username)

    for item in query_result:
        from_student = item.from_student.user.username
        student_name = item.from_student.user.first_name + ' ' + item.from_student.user.last_name
        student_email = item.from_student.user.email
        course = item.course
        time = item.created_timestamp
        str_time = time.strftime("sent on %m-%d-%Y at %H:%M:%S")
        status = 'Pending' if item.status == 1 else 'Accepted' if item.status == 2 else 'Declined'
        date = item.date_requested
        start = item.start_time_requested
        end = item.end_time_requested
        request_list.append({'from_student':from_student, 'student_name':student_name, 'course':course, 'status':status, 'student_email':student_email, 'time':str_time, 'date': date, 'start': start, 'end':end})

    context = {'request_list':request_list}
    return render(request, 'tutorme/tutorRequestsView.html', context)

# tutor view classes page (My Classes)
def tutor_my_classes_view(request):
    if not check_logged_in(request):
        return render(request, 'tutorme/index.html', None)


    course_list = []
    curr_user = request.user.username
    current_tutor = AppUser.objects.filter(user__username__contains = curr_user).first()

    # handles clicking "Remove" button in any card in the My Classes page in the Tutor View,
    # removes the corresponding entry from the Tutor model in the database
    if request.method == 'POST':
        curr_user = request.user.username
        current_tutor = AppUser.objects.filter(user__username__contains = curr_user).first()
        remove_course = request.POST.get('course')
        
        tutor_to_remove = Tutor.objects.filter(
            user = current_tutor,
            course = remove_course
        ).delete()

    # queries database for list of all courses the tutor teaches in the Tutor model, 
    # displaying all of them as cards in the My Classes page in the Tutor View
    course_query = Tutor.objects.filter(
        user = current_tutor
    )

    for item in course_query:
        course = item.course
        course_list.append(course)

    context = {'course_list' : course_list}
    return render(request, 'tutorme/tutorMyClassesView.html', context)


# tutor view search classes (Add Classes)
def tutor_add_classes_view(request):
    if not check_logged_in(request):
        return render(request, 'tutorme/index.html', None)

    classList = []
    searchParams = ''

    # handles clicking "Add" button in a table row that displays search results, 
    # adds Tutor entry to database based on the course the tutor wants to teach
    if request.method == 'POST':
        course = request.POST.get('course')
        curr_user = request.user.username
        current_tutor = AppUser.objects.filter(user__username__contains = curr_user).first()
        monday_times = request.POST.get('mondayTimes')
        tuesday_times = request.POST.get('tuesdayTimes')
        wednesday_times = request.POST.get('wednesdayTimes')
        thursday_times = request.POST.get('thursdayTimes')
        friday_times = request.POST.get('fridayTimes')
        new_tutor, created = Tutor.objects.get_or_create(
            user = current_tutor,
            course = course,
        )
      
        new_tutor.save()

    # handles clicking "Search" button in the Add Classes page in the Tutor View,
    # queries SIS API based on search parameters enetered in the search bar, displays classes in table view
    if request.method == 'GET' and 'search' in request.GET:
        searchParams = request.GET.get('search', '')
        classList = sisapi.search_matcher(searchParams)

    context = {'classList': classList, 'search':searchParams}
    return render(request, 'tutorme/tutorAddClassesView.html', context)

def tutor_profile_view(request):
    if not check_logged_in(request):
        return render(request, 'tutorme/index.html', None)

    classes_list = []
    ratings_list = []
    bio_list = []
    hourly_rate = 10.00
    tutor_user_id = request.user.id
    tutor_app_id = AppUser.objects.filter(user_id__id = tutor_user_id).values('id')[0]['id']
    rating_query_result = Ratings.objects.filter(tutor_who_was_rated__id = tutor_app_id)
    classes_query_result = Tutor.objects.filter(user_id__id = tutor_app_id)
    tutor_query_result = AppUser.objects.filter(user_id__id = tutor_user_id)

    entry_exists = TutorTimes.objects.filter(user_id__id = tutor_app_id).exists()
    if entry_exists:
        tutor_times_query = TutorTimes.objects.get(user_id__id = tutor_app_id)
        hourly_rate = tutor_times_query.hourly_rate
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
    bio_list.append({'bio': tutor_query_result[0].bio})
    context = {'ratings_list': ratings_list, 'classes_list': classes_list, 'bio_list': bio_list, 'hourly_rate': hourly_rate}
    return render(request, 'tutorme/tutorProfile.html', context)

def student_profile_view(request):
    if not check_logged_in(request):
        return render(request, 'tutorme/index.html', None)

    bio_list = []
    help_list = []
    user = request.user.id
    student_app_id = AppUser.objects.filter(user_id__id = user).values('id')[0]['id']
    student_profile_query = AppUser.objects.filter(user_id__id=user)[0]
    year = student_profile_query.year
    stu_bio = student_profile_query.bio
    stu_help_descr = student_profile_query.help_description
    bio_list.append({'bio':stu_bio})
    help_list.append({'help': stu_help_descr})
    class_request_query = Request.objects.filter(from_student=student_app_id)
    courses_requested_list = []
    for class_requested in class_request_query:
        course = class_requested.course
        courses_requested_list.append({'course':course})
    context = {'courses_requested': courses_requested_list, 'bio_list': bio_list, 'year': year, 'help_description': stu_help_descr}
    return render(request, 'tutorme/studentProfile.html', context)

def edit_profile_view(request):
    if not check_logged_in(request):
        return render(request, 'tutorme/index.html', None)

    if request.method == 'POST':
        bio = request.POST.get('bioText')
        help_description_test = request.POST.get('helpText')
        student_year = request.POST.get('studentYear')
        current_student = AppUser.objects.get(user_id__id = request.user.id)
        current_student.bio = bio
        current_student.year = student_year
        current_student.help_description = help_description_test
        current_student.save()
    return render(request, 'tutorme/editProfile.html')

def edit_tutor_profile_view(request):
    if not check_logged_in(request):
        return render(request, 'tutorme/index.html', None)

    tutor_user_id = request.user.id

    if request.method == 'POST':
        bio = request.POST.get('bio')
        hourly_rate = request.POST.get('hourlyRate')
        print(bio)
        print(hourly_rate)
        tutor_app_id = AppUser.objects.filter(user_id__id = tutor_user_id).values('id')[0]['id']
        
        current_tutor_change_bio = AppUser.objects.get(user_id__id = tutor_user_id)

        current_tutor_change_bio.bio = bio
        entry_exists = TutorTimes.objects.filter(user_id__id = tutor_app_id).exists()
        if entry_exists and hourly_rate is not None:
            current_tutor_change_rate = TutorTimes.objects.get(user_id__id = tutor_app_id)
            current_tutor_change_rate.hourly_rate = hourly_rate
            current_tutor_change_rate.save()

        current_tutor_change_bio.save()

    return render(request, 'tutorme/editTutorProfile.html')

def add_tutor_available_times(request):
    user_id = request.user.id
    current_times_list = []
    tutor_app_id = AppUser.objects.filter(user_id__id = user_id).values('id')[0]['id']
    current_times = TutorTimes.objects.get(user_id__id = tutor_app_id).available_times
    
    if request.method == 'POST':
        user_id = request.user.id
        tutor_app_id = AppUser.objects.filter(user_id__id = user_id).values('id')[0]['id']
        curr_user = request.user.username
        current_tutor = AppUser.objects.filter(user__username__contains = curr_user).first()
        monday_times = request.POST.get('mondayTimes')
        tuesday_times = request.POST.get('tuesdayTimes')
        wednesday_times = request.POST.get('wednesdayTimes')
        thursday_times = request.POST.get('thursdayTimes')
        friday_times = request.POST.get('fridayTimes')
        new_tutor, created = TutorTimes.objects.get_or_create(
            user = current_tutor
        )
        new_tutor.available_times = {
            'Monday': monday_times,
            'Tuesday': tuesday_times,
            'Wednesday': wednesday_times,
            'Thursday': thursday_times,
            'Friday': friday_times
        }
        new_tutor.save()
    context = {'available_times_dict': current_times}
    return render(request, 'tutorme/tutorAddTimes.html',context)

def apply_to_be_a_tutor(request):
    print('ran out here')
    if request.method == "POST":
        print('new tutor made')
        user_id = request.user.id
        user_to_change =  AppUser.objects.get(user_id__id = user_id)
        user_to_change.user_type = 2
        user_to_change.save()

        app_id = AppUser.objects.filter(user_id__id = user_id).values('id')[0]['id']

        #remove all requests made by student becoming a tutor
        remove_query = Request.objects.filter(
            from_student = app_id,
        ).delete()
        
        #enter new tutor into tutorTimes table
        new_tutor_user = AppUser.objects.get(id = app_id)

        new_tutor, created = TutorTimes.objects.get_or_create(
            user = new_tutor_user,
        )
        new_tutor.available_times =  {
                                    'Monday':[],
                                    'Tuesday': [],
                                    'Wednesday': [],
                                    'Thursday': [],
                                    'Friday': []
                                    }
        new_tutor.hourly_rate = 10.00
        new_tutor.save()
    
    return render(request, 'tutorme/applyToBeATutor.html')