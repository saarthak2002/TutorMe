from django.test import TestCase, Client
from .models import Tutor, AppUser, Request, Ratings
from tutorme import views
from django.contrib.auth.models import User
from django.urls import reverse

server = "127.0.0.1" #"https://tutor-me-a29.herokuapp.com/tutorme/"
# returns a client with the tutor logged in
def login_as_tutor(self):
    c = Client(SERVER_NAME=server)
    c.get('/tutorme/')
    username_tutor='test_user_tutor'
    password_tutor='tutor_password'

    # try logging in if the user already exists
    if c.login(username=username_tutor, password=password_tutor):
        test_user = User.objects.get(username=username_tutor)
        return c, test_user

    # create a tutor user
    test_user, tutor_created = User.objects.get_or_create(username=username_tutor, email='', password=password_tutor)
    self.assertTrue(tutor_created)
    test_user.save()

    # log in as the tutor
    logged_in = c.login(username=username_tutor, password=password_tutor)
    self.assertTrue(logged_in)
    return c, test_user

# add a course to the tutor profile
def add_tutor_course(client, course):
    client.post(reverse(views.tutor_add_classes_view), {'course': course})


class TutorMyClassesViewTests(TestCase):

    def test_course_on_tutor_profile(self):
        course_name = "Calculus I"
        client, tutor = login_as_tutor(self)

        # add the course to the tutor profile
        add_tutor_course(client, course_name)

        # check the course appears on the tutor profile
        response = client.get(reverse(views.tutor_my_classes_view)) #client.get('https://tutor-me-a29.herokuapp.com/tutorme/tutor/myclasses')
        self.assertContains(response, course_name)

"""
class TutorAddClassesViewTests(TestCase):

    def test_search_courses_by_mnemonic(self):
        # search courses with MATH mnemonic
        # only MATH courses appear

    def test_search_courses_by_number(self):
        # search courses with number MATH 1140
        # only courses with number 1140 appear

    def test_search_courses_by_name(self):
        # search courses with name 'Financial'
        # the course 'Financial Mathematics' appears

class TutorRequestsViewTests(TestCase):
    
    def test_display_pending_request():
        # create request
        # check it appears on the page

    def test_accept_request():
        # create request
        # click accept button
        # check request status is accept

    def test_reject_request():
        # create request
        # click reject button
        # check request status is reject


class TutorProfileView(TestCase):

    def test_rating(self):
        # create rating for tutor
        # check rating appears on profile
    

class StudentRequestsView():

    def test_remove_request():
        # create request
        # remove request by clicking button
        # check the request no longer exists

    def test_display_request():
        # create request
        # check the request is shown on the page
"""
