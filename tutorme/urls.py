from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name="tutorme/index.html")),
    path('accounts/google/login/callback/tutorme/', TemplateView.as_view(template_name="tutorme/index.html")),
    path('accounts/social/signup/tutorme/', TemplateView.as_view(template_name="tutorme/index.html")),
    path('accounts/logout/tutorme/', TemplateView.as_view(template_name="tutorme/index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
]
