# Generated by Django 4.2 on 2023-04-23 17:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0001_initial'),
        ('store', '0004_alter_book_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_borrowed', models.DateField(default=django.utils.timezone.now)),
                ('date_due', models.DateField()),
                ('date_returned', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='store.book')),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to='UserProfile.userprofile')),
            ],
        ),
    ]