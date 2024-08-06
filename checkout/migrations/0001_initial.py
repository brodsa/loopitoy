# Generated by Django 3.2.25 on 2024-08-06 20:08

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        ('toys', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('street_address', models.CharField(max_length=80)),
                ('town_or_city', models.CharField(max_length=254)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('county', models.CharField(blank=True, max_length=80, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('delivery_cost', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('grand_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('original_bag', models.TextField(default='')),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='checkout.order')),
                ('toy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toys.toys')),
            ],
        ),
    ]
