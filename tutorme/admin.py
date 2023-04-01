from django.contrib import admin
from .models import AppUser, Tutor, Request, Student_Profile
# Register your models here.

admin.site.register(AppUser)
admin.site.register(Tutor)
admin.site.register(Request)
admin.site.register(Student_Profile)
