from django.contrib import admin
from .models import Section, Author, Articles

# Register your models here.
admin.site.register(Section)
admin.site.register(Author)
admin.site.register(Articles)