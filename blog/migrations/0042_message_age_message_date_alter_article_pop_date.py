# Generated by Django 5.1.3 on 2024-11-27 13:48

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_message_created_at_alter_article_pop_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='article',
            name='pop_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 27, 13, 48, 40, 324029, tzinfo=datetime.timezone.utc)),
        ),
    ]