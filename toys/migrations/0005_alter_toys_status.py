# Generated by Django 3.2.25 on 2024-06-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0004_alter_toys_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toys',
            name='status',
            field=models.CharField(choices=[('open', 'OPEN'), ('declaim', 'DECLAIM'), ('eshop', 'E-SHOP'), ('sold', 'SOLD'), ('paid', 'PAID'), ('in_bag', 'IN_BAG')], default='open', max_length=50),
        ),
    ]
