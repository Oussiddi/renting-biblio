# Generated by Django 4.2 on 2023-05-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_bookcopy_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookcopy',
            name='reserved',
            field=models.BooleanField(default=False),
        ),
    ]
