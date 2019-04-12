from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# kwagrs accepts any keyword argument onto end of function
# When a user is saved, then send this signal to receiver. Receiver is the create profile function.
# If that user was created, create profile object with user equal to the instance


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if created:
        instance.profile.save()
