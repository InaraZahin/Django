# Generated by Django 2.2.7 on 2019-12-05 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inaraApp', '0024_auto_20191205_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
