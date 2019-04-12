from django.contrib import admin
from .models import Profile

# Adds profile to our Admin page
admin.site.register(Profile)
