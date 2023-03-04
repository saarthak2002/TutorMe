from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('accounts/google/login/callback/tutorme/', index),
    path('accounts/social/signup/tutorme/', index),
    path('accounts/logout/tutorme/', index),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]
