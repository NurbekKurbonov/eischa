# Generated by Django 4.0 on 2021-12-25 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('secondadmin', '0002_addc_delete_country'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='addc',
            new_name='Davlatlar',
        ),
    ]