from django.contrib import admin
from .models import AppUser, Tutor, Request
# Register your models here.

admin.site.register(AppUser)
admin.site.register(Tutor)
admin.site.register(Request)
