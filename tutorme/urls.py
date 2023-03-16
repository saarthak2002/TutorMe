from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import index, student_requests_view, tutor_requests_view, tutor_my_classes_view, tutor_add_classes_view

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
]
