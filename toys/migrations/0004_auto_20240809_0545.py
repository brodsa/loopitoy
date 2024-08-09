# Generated by Django 3.2.25 on 2024-08-09 05:45

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0003_alter_toys_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toys',
            name='image',
        ),
        migrations.AddField(
            model_name='toys',
            name='picture',
            field=django_resized.forms.ResizedImageField(crop=None, default='media/placeholder.webp', force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[400, None], upload_to='media/toys'),
        ),
    ]
