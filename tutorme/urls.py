from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import index, student_requests_view

urlpatterns = [
    path('', index, name='index'),
    path('accounts/google/login/callback/tutorme/', index),
    path('accounts/google/login/callback/tutorme/requests/', student_requests_view),
    path('requests/', student_requests_view),
    path('accounts/social/signup/tutorme/', index),
    path('accounts/logout/tutorme/', index),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]
