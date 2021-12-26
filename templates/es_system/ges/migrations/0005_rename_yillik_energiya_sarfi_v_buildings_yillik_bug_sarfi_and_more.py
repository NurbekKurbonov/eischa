# Generated by Django 4.0 on 2021-12-17 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ges', '0004_v_buildings_delete_val_buildings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='v_buildings',
            old_name='yillik_energiya_sarfi',
            new_name='yillik_bug_sarfi',
        ),
        migrations.RenameField(
            model_name='v_buildings',
            old_name='yillik_issiqlik_sarfi',
            new_name='yillik_elektr_sarfi',
        ),
        migrations.RemoveField(
            model_name='v_buildings',
            name='jihozlanganligi',
        ),
        migrations.AddField(
            model_name='v_buildings',
            name='yillik_issiq_suv_sarfi',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
    ]
