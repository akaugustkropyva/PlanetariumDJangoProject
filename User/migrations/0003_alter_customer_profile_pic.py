# Generated by Django 4.1.7 on 2023-05-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='images/default_user.jpg', upload_to=''),
        ),
    ]
