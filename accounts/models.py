from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import hashlib
from biodata.models import Biodata


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    favourite = models.ManyToManyField(Biodata, related_name='favourite', default=None, blank=True)

    def __str__(self):
        return self.user.email

class EmailConfirmed(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=500)
    email_confirmd = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = 'User Email-Confirmed'


@receiver(post_save, sender=User)
def create_user_email_confirmation(sender, instance, created, **kwargs):
    if created:
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        email_confirmed_instance = EmailConfirmed(user = instance)
        user_encoded = f'{instance.email}-{dt}'.encode()
        activation_key = hashlib.sha224(user_encoded).hexdigest()
        email_confirmed_instance.activation_key = activation_key
        email_confirmed_instance.save()