# Generated by Django 4.0.4 on 2022-04-25 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizzauser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
