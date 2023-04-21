from django.db import models


# Create your models here.
class Section(models.Model):
    rubric = models.CharField(max_length=30)
    article_title = models.CharField(max_length=35)
    article_text = models.TextField()
    views = models.IntegerField()


class Author(models.Model):
    full_name = models.CharField(max_length=60)
    position = models.CharField(max_length=55)
    employment_contract = models.IntegerField()
    phone = models.CharField(max_length=13)


class Articles(models.Model):
    title = models.CharField(max_length=60)
    price = models.FloatField(default=0.0)
    composition = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
