# Generated by Django 5.0 on 2024-04-30 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_availabe',
            new_name='is_available',
        ),
    ]