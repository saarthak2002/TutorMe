from django.test import TestCase, Client
from .models import Tutor, AppUser, Request, Ratings
from tutorme import views
from django.contrib.auth.models import User
from django.urls import reverse

server = "tutor-me-a29.herokuapp.com" #"127.0.0.1" 
# returns a student user
def create_student():
    username_student='test_user_student'
    password_student='student_password'

    try:
        test_user = User.objects.get(username=username_student, email='', password=password_student)
        test_student = AppUser.objects.get(user=test_user)

    except:
        test_user = User.objects.create_user(username=username_student, email='', password=password_student)
        test_user.save()
        test_student = AppUser.objects.get(user=test_user)
        test_student.user_type = 1
        test_student.save()
    
    return test_student

# returns a client with the tutor logged in
def login_as_tutor():
    c = Client(SERVER_NAME=server)
    c.get('/tutorme/')
    username_tutor='test_user_tutor'
    password_tutor='tutor_password'

    # try logging in if the user already exists
    if c.login(username=username_tutor, password=password_tutor):
        test_user = User.objects.get(username=username_tutor)
        test_tutor = AppUser.objects.get(user=test_user)
        return c, test_tutor

    # create a tutor user
    
    test_user = User.objects.create_user(username=username_tutor, email='', password=password_tutor)
    test_user.save()
    test_tutor = AppUser.objects.get(user=test_user)
    test_tutor.user_type = 2
    test_tutor.save()

    # log in as the tutor
    c.login(username=username_tutor, password=password_tutor)
    return c, test_tutor

# add a course to the tutor profile
def add_tutor_course(client, course):
    client.post(reverse(views.tutor_add_classes_view), {'course': course})


class TutorMyClassesViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client, cls.tutor = login_as_tutor()

    def setUp(self):
        self.client = TutorMyClassesViewTests.client

    def test_course_on_tutor_profile(self):
        course_name = "Calculus I"

        # add the course to the tutor profile
        add_tutor_course(self.client, course_name)

        # check the course appears on the tutor profile
        response = self.client.get(reverse(views.tutor_my_classes_view)) 
        self.assertContains(response, course_name)

class TutorAddClassesViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client, cls.tutor = login_as_tutor()

    def setUp(self):
        self.client = TutorAddClassesViewTests.client

    def test_search_courses_by_mnemonic(self):
        # search courses with MATH mnemonic
        response = self.client.get(reverse(views.tutor_add_classes_view), {'search': 'MATH'}) 
        # MATH courses appear
        self.assertContains(response, 'MATH')

    def test_search_courses_by_number(self):
        # search courses with number MATH 1140
        response = self.client.get(reverse(views.tutor_add_classes_view), {'search': 'MATH 1140'}) 
        # courses with number 1140 appear
        self.assertContains(response, '1140')

    def test_search_courses_by_name(self):
        # search courses with name 'Financial'
        response = self.client.get(reverse(views.tutor_add_classes_view), {'search': 'Financial Math'}) 
        # the course 'Financial Mathematics' appears
        self.assertContains(response, 'Financial Mathematics')
        self.assertContains(response, '1140')
        self.assertContains(response, 'MATH')

class TutorRequestsViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client, cls.tutor = login_as_tutor()
        cls.student = create_student()
        cls.course = 'Test course'
    
    def setUp(self):
        self.client = TutorRequestsViewTests.client
        # create request
        self.tutoring_request = Request.objects.create(from_student=self.student, to_tutor=self.tutor, course=self.course)
        # navigate to request view
        self.response = self.client.get(reverse(views.tutor_requests_view)) 

    def test_display_pending_request(self):
        # check it appears on the page
        self.assertContains(self.response, self.course)

    def test_accept_request(self):
        # accept request 
        self.tutoring_request.status = 2
        self.tutoring_request.save()
        #reload page
        self.response = self.client.get(reverse(views.tutor_requests_view)) 
        # check request status is accept
        self.assertContains(self.response, 'Accepted')

    def test_reject_request(self):
        # reject request 
        self.tutoring_request.status = 3
        self.tutoring_request.save()
        #reload page
        self.response = self.client.get(reverse(views.tutor_requests_view)) 
        # check request status is declined
        self.assertContains(self.response, 'Declined')


class TutorProfileView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client, cls.tutor = login_as_tutor()
        cls.student = create_student()

    def setUp(self):
        self.client = TutorProfileView.client

    def test_rating(self):
        rating_level = 4
        rating_review = 'This is a test rating'
        # create rating for tutor
        self.rating = Ratings.objects.create(student_who_rated=self.student, tutor_who_was_rated=self.tutor, rating=rating_level, review=rating_review)
        self.rating.save()
        # check rating appears on profile
        response = self.client.get(reverse(views.tutor_profile_view)) 
        self.assertContains(response, rating_level)
        self.assertContains(response, rating_review)
    
"""
class StudentRequestsView():

    def test_remove_request():
        # create request
        # remove request by clicking button
        # check the request no longer exists

    def test_display_request():
        # create request
        # check the request is shown on the page
"""
