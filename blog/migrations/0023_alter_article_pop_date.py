# Generated by Django 5.1.3 on 2024-11-14 10:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_article_pop_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pop_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 14, 10, 35, 53, 472304, tzinfo=datetime.timezone.utc)),
        ),
    ]
