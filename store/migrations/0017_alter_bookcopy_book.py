# Generated by Django 4.2 on 2023-05-12 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_bookcopy_reserved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcopy',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='copies', to='store.book'),
        ),
    ]
