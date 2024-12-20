# Generated by Django 5.1.3 on 2024-11-14 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_alter_article_pop_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='pop_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 14, 12, 22, 22, 588165, tzinfo=datetime.timezone.utc)),
        ),
    ]
