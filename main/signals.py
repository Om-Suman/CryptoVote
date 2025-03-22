# main/signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.apps import apps

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile = apps.get_model('main', 'Profile')  # Dynamic import here
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    Profile = apps.get_model('main', 'Profile')  # Dynamic import here
    instance.profile.save()
