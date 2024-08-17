# Generated by Django 5.0.6 on 2024-08-17 06:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminside', '0006_userprofile_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Adminside.product')),
            ],
        ),
    ]