# Generated by Django 5.1.3 on 2024-11-14 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_article_pop_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='floatfield',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='myfile',
            field=models.BinaryField(default=None),
        ),
        migrations.AlterField(
            model_name='article',
            name='pop_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 14, 8, 10, 48, 322471, tzinfo=datetime.timezone.utc)),
        ),
    ]
