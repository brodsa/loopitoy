# Generated by Django 3.2.25 on 2024-06-28 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
        ('toys', '0006_alter_toys_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='toys',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sells', to='profiles.userprofile'),
        ),
        migrations.AlterField(
            model_name='toys',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='toy_seller', to=settings.AUTH_USER_MODEL),
        ),
    ]