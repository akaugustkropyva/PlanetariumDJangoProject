# Generated by Django 4.1.7 on 2023-05-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_order_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='date_event',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
