from django.db import models
from ckeditor.fields import RichTextField


class Quotes(models.Model):
    title = models.TextField()
    description = RichTextField()

    def __str__(self):
        return self.title[:35]+"..."