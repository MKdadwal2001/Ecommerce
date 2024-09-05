# Generated by Django 5.0.6 on 2024-08-30 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminside', '0008_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='is_replied',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='reply',
            field=models.CharField(default='', max_length=255),
        ),
    ]