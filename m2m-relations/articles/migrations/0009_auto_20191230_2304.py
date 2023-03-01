# Generated by Django 2.2.5 on 2019-12-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20191230_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='chains',
            field=models.ManyToManyField(related_name='chains', through='articles.ArticleSection', to='articles.Article'),
        ),
    ]
