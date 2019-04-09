from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Each class is going to be its own table


class Post(models.Model):
    # Field of our table is a character
    title = models.CharField(max_length=100)
    content = models.TextField()
    datePosted = models.DateTimeField(default=timezone.now)
    # If a user is deleted then we want to delete the post
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
