from django.db import models
from django.contrib.auth.models import User

# Whenever you make model changes, must migrate the database


class Profile(models.Model):
    # Sets one-to-one relationship. If user is deleted, delee the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
