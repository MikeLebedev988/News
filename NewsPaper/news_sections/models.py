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

    # articles = models.ManyToManyField('Articles', through='SectionArticles')  # Why we do relationship 'ManyToMany' below in one point? What we have if we do it here?
    # And what we have with that after trying 'makemigrations' :
    # ERRORS:
    #         HINT: Rename field 'news_sections.Section.articles', or add/change a related_name argument to the definition for field 'news_sections.Articles.section'.
    # news_sections.Section.articles: (fields.E303) Reverse query name for 'news_sections.Section.articles' clashes with field name 'news_sections.Articles.section'.
    #         HINT: Rename field 'news_sections.Articles.section', or add/change a related_name argument to the definition for field 'news_sections.Section.articles'.


class Author(models.Model):
    full_name = models.CharField(max_length=60)
    position = models.CharField(max_length=2, choices=POSITIONS, default=journalist)
    employment_contract = models.IntegerField()
    phone = models.CharField(max_length=13)


class Articles(models.Model):
    title = models.CharField(max_length=60)
    price = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    editing = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    section = models.ManyToManyField(Section, through='SectionArticles')  # First relationship 'ManyToMany'.


class SectionArticles(models.Model):
    amount = models.IntegerField(default=1)
    section = models.ForeignKey(Articles, on_delete=models.CASCADE)
    articles = models.ForeignKey(Section, on_delete=models.CASCADE)
