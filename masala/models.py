from django.db import models
from ckeditor.fields import RichTextField


class masala_catagory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class masala(models.Model):
    question = models.TextField()
    answer = RichTextField()
    writter = models.CharField(max_length=255)
    catagory = models.ForeignKey(masala_catagory, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.question[:50]+"..."

class Hadith(models.Model):
    hadith = models.TextField()
    reference = models.TextField()

    def __str__(self):
        return self.hadith[:50]+"..."
