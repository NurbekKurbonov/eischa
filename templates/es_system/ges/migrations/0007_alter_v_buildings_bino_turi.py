# Generated by Django 4.0 on 2021-12-17 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ges', '0006_remove_v_buildings_isitish_turi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='v_buildings',
            name='bino_turi',
            field=models.CharField(max_length=266),
        ),
    ]
