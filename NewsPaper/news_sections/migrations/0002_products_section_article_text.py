# Generated by Django 4.2 on 2023-04-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_sections', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.FloatField(default=0.0)),
                ('composition', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='article_text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]