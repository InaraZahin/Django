# Generated by Django 2.2.7 on 2019-11-27 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inaraApp', '0002_home_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='fourth',
            field=models.TextField(blank=True, max_length=520, null=True),
        ),
    ]
