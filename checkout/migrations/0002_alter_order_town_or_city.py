# Generated by Django 3.2.25 on 2024-06-25 19:22

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='town_or_city',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
