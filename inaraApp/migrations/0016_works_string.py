# Generated by Django 2.2.7 on 2019-12-01 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inaraApp', '0015_works'),
    ]

    operations = [
        migrations.AddField(
            model_name='works',
            name='string',
            field=models.TextField(blank=True, max_length=520, null=True),
        ),
    ]
