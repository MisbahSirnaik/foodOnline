from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance) # creates a user profile as soon as user is created
    else:
        try :
            profile = UserProfile.objects.get(user=instance) # when user profile is updated
            profile.save()
        except :
            # creates user profile if doesn't exist
            UserProfile.objects.create(user=instance)

# post_save.connect(post_save_create_profile_receiver, sender=User)