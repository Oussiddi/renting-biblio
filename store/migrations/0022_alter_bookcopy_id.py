# Generated by Django 4.2 on 2023-05-14 10:06

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_bookcopy_id_delete_rental'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcopy',
            name='id',
            field=models.UUIDField(default=store.models.BookCopy.generate_uuid, editable=False, primary_key=True, serialize=False),
        ),
    ]
