# Generated by Django 5.1.3 on 2024-11-10 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(db_column='mytitle', help_text='enter title', max_length=70, unique=True),
        ),
    ]
