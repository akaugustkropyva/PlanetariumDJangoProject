# Generated by Django 4.1.7 on 2023-05-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_order_card_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.FloatField(default=0, null=True),
        ),
    ]
