# Generated by Django 2.2.7 on 2019-12-01 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inaraApp', '0017_testi'),
    ]

    operations = [
        migrations.AddField(
            model_name='testi',
            name='bgimage',
            field=models.ImageField(blank=True, null=True, upload_to='home/'),
        ),
        migrations.AddField(
            model_name='testi',
            name='client1',
            field=models.ImageField(blank=True, null=True, upload_to='home/'),
        ),
        migrations.AddField(
            model_name='testi',
            name='client2',
            field=models.ImageField(blank=True, null=True, upload_to='home/'),
        ),
        migrations.AddField(
            model_name='testi',
            name='client3',
            field=models.ImageField(blank=True, null=True, upload_to='home/'),
        ),
    ]