# Generated by Django 5.1.3 on 2024-11-11 04:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_article_pop_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pop_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 11, 4, 27, 24, 128778, tzinfo=datetime.timezone.utc)),
        ),
    ]
