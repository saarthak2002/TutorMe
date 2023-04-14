from django.contrib import admin
from .models import AppUser, Tutor, Request, Ratings, TutorTimes
# Register your models here.

admin.site.register(AppUser)
admin.site.register(Tutor)
admin.site.register(TutorTimes)
admin.site.register(Request)
admin.site.register(Ratings)
