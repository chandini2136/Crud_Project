# Generated by Django 4.2.6 on 2023-12-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_capital'),
    ]

    operations = [
        migrations.AddField(
            model_name='capital',
            name='population',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
