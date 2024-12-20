# Generated by Django 5.1.3 on 2024-11-27 13:22

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_message_alter_article_pop_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='pop_date',
            field=models.DateField(default=datetime.datetime(2024, 11, 27, 13, 21, 50, 646757, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
