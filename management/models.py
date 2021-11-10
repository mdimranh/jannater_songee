from django.db import models
from django.db.models.fields import BooleanField
from django.utils.timezone import now


ACTIONS = (
    ('no', 'no'),
    ('progress', 'progress'),
    ('done', 'done')
)

class Message(models.Model):
    name = models.CharField(max_length=250)
    subject = models.TextField()
    message = models.TextField()
    send_at = models.DateTimeField(default=now)
    seen = models.BooleanField(default=False)
    action = models.CharField(max_length=250 ,choices=ACTIONS, default='no')

    def __str__(self):
        return self.name
