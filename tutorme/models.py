from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'tutor'),
    )
    bio = models.TextField(default="Hi, I'm excited to use TutorMe!")
    YEAR_CHOICES = [
    (1, 'First Year'),
    (2, 'Second Year'),
    (3, 'Third Year'),
    (4, 'Fourth Year'),
    (5, 'Graduate')
    ]
    year = models.CharField(default=1, max_length=12, choices=YEAR_CHOICES)
    help_description = models.TextField(default="I am looking for a tutor")
    user_type = models.PositiveSmallIntegerField(default=1, choices=USER_TYPE_CHOICES)
    def __str__(self):
        return self.user.username + ' - ' + ('Tutor' if self.user_type == 2 else 'Student')

@receiver(post_save, sender=User)
def app_user_create(sender, instance=None, created=False, **kwargs):
    if created:
        AppUser.objects.create(user=instance,)

class Tutor(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    course = models.CharField(max_length=150)
    def __str__(self):
        return self.user.user.username + ' - ' + self.course
    
class Request(models.Model):
    created_timestamp = models.DateTimeField(auto_now_add=True)
    from_student = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='from_student')
    to_tutor = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='to_tutor')
    course = models.CharField(max_length=150)
    REQUEST_STATUS_CHOICES = (
      (1, 'pending'),
      (2, 'accepted'),
      (3, 'declined')
    )
    status = models.PositiveSmallIntegerField(choices=REQUEST_STATUS_CHOICES, default=1)
    date_requested = models.DateField(default=datetime.now)
    start_time_requested = models.TimeField(default=datetime.now)
    end_time_requested = models.TimeField(default=datetime.now)
    def __str__(self):
        return 'from: ' + self.from_student.user.username + ' to: ' + self.to_tutor.user.username + ' course: ' + self.course + ' status: ' + ('pending' if self.status == 1 else 'accepted' if self.status == 2 else 'declined')
    
    
class Ratings(models.Model):
  created_timestamp_rating = models.DateTimeField(auto_now_add=True)
  student_who_rated = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='student_who_rated')
  tutor_who_was_rated = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='tutor_who_was_rated')
  RATING_CHOICES = [
    (1, 'Poor'),
    (2, 'Fair'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
  ]
  rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=3)
  review = models.CharField(max_length=500, default='')
  
  def __str__(self):
        return 'from: ' + self.student_who_rated.user.username + ' to: ' + self.tutor_who_was_rated.user.username + ' rating: ' + ('Poor' if self.rating == 1 else 'Fair' if self.rating == 2 else 'Good' if self.rating == 3 else 'Very Good' if self.rating == 4 else 'Excellent') + ' review: ' + self.review

# class Student_Profile(models.Model):
#   user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
#   YEAR_CHOICES = [
#     (1, 'First Year'),
#     (2, 'Second Year'),
#     (3, 'Third Year'),
#     (4, 'Fourth Year'),
#     (5, 'Graduate')
#   ]
#   year = models.CharField(max_length=12, choices=YEAR_CHOICES)
#   help_description = models.TextField()
#   bio = models.TextField()
#   def __str__(self):
#       return str(self.student_profile)
