# Generated by Django 3.2.25 on 2024-06-09 11:34

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0003_auto_20240609_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toys',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='media/placeholder.placeholder.webp', force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[400, None], upload_to='media/toys'),
        ),
    ]
