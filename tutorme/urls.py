from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import index, student_requests_view, tutor_requests_view, tutor_my_classes_view, tutor_add_classes_view, tutor_profile_view, student_profile_view, edit_profile_view, edit_tutor_profile_view, add_tutor_available_times, apply_to_be_a_tutor, leave_a_review

urlpatterns = [
    path('', index, name='index'),
    path('accounts/google/login/callback/tutorme/', index),
    path('accounts/google/login/callback/tutorme/requests/', student_requests_view),
    path('requests/', student_requests_view),
    path('tutor/requests/', tutor_requests_view),
    path('tutor/myclasses/', tutor_my_classes_view),
    path('tutor/classes/', tutor_add_classes_view),
    path('accounts/social/signup/tutorme/', index),
    path('accounts/logout/tutorme/', index),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('tutor/profiles/', tutor_profile_view),
    path('profile/', student_profile_view),
    path('profile/edit', edit_profile_view),
    path('tutor/profiles/edit', edit_tutor_profile_view),
    path('tutor/chooseAvailableTimes/', add_tutor_available_times), 
    path('applyToBeATutor/', apply_to_be_a_tutor),
    path('review/', leave_a_review)
]
