from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class AppUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'tutor'),
    )
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
    