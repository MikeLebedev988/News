from django.db import models

director = 'DI'
admin = 'AD'
lead_journalist = 'LJ'
journalist = "JO"
editor = 'ED'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (lead_journalist, 'Ведущий журналист'),
    (journalist, 'Журналист'),
    (editor, 'Редактор'),
]


# Create your models here.
class Section(models.Model):
    rubric = models.CharField(max_length=30)
    article_title = models.CharField(max_length=35)
    article_text = models.TextField()
    views = models.IntegerField()


class Author(models.Model):
    full_name = models.CharField(max_length=60)
    position = models.CharField(max_length=2, choices=POSITIONS, default=journalist)
    employment_contract = models.IntegerField()
    phone = models.CharField(max_length=13)


class Articles(models.Model):
    title = models.CharField(max_length=60)
    price = models.FloatField(default=0.0)
    composition = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
