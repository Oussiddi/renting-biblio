# Generated by Django 4.2 on 2023-05-14 11:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_bookcopy_sku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookcopy',
            name='sku',
        ),
        migrations.AlterField(
            model_name='bookcopy',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
