from django.db import models


# Create your models here.
class Section(models.Model):
    rubric = models.CharField(max_length=30)
    article_title = models.CharField(max_length=35)
    article_text = models.TextField()
    views = models.IntegerField()
