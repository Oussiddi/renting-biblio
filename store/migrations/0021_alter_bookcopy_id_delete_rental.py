# Generated by Django 4.2 on 2023-05-14 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_bookcopy_rented'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcopy',
            name='id',
            field=models.UUIDField(default='91b70d9f7dfc47a4', editable=False, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
    ]