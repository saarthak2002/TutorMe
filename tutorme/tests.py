from django.test import TestCase, Client
from .models import Tutor, AppUser, Request, Ratings
from django.contrib.auth.models import UserManager

# returns a client with the tutor logged in
def login_as_tutor():
    c = Client()
    username_tutor='test_user_tutor'
    password_tutor='test_user_tutor_password'

    # try logging in if the user already exists
    if c.login(username_tutor, password_tutor):
        return c

    # create a tutor user
    test_user = UserManager.create_user(username=username_tutor, email=None, password=password_tutor)
    AppUser.objects.get_or_create(user=test_user, user_type=2)

    # log in as the tutor
    c.login(username_tutor, password_tutor)
    return c

class TutorMyClassesViewTests(TestCase):

    def test_course_on_tutor_profile(self):
        login_as_tutor()
        # add a course to the tutor profile
        # check the course appears on the tutor profile

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
