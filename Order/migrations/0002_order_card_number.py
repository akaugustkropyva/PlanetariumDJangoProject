# Generated by Django 4.1.7 on 2023-05-23 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='card_number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
