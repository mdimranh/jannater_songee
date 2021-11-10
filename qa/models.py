from django.db import models
from ckeditor.fields import RichTextField


class qa(models.Model):
    question = models.TextField()
    answer = RichTextField()

    def __str__(self):
        return self.question[:25]+"..."
