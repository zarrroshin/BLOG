# Generated by Django 5.1.3 on 2024-11-11 04:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_article_pop_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pop_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 11, 4, 28, 46, 267994, tzinfo=datetime.timezone.utc)),
        ),
    ]
