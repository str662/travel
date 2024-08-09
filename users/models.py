from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user}'
