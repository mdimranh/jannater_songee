from django.db import models
from biodata.models import Biodata
from ckeditor.fields import RichTextField
from django.utils.timezone import now

class Post(models.Model):
    user = models.ForeignKey(Biodata, on_delete=models.CASCADE, related_name='user')
    tag = models.ForeignKey(Biodata, on_delete=models.CASCADE, related_name='tag')
    post = RichTextField()
    create_on = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.name

