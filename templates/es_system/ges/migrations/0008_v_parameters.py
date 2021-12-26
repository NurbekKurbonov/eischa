# Generated by Django 4.0 on 2021-12-17 20:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ges', '0007_alter_v_buildings_bino_turi'),
    ]

    operations = [
        migrations.CreateModel(
            name='v_parameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=266)),
                ('sana', models.DateField(default=django.utils.timezone.now)),
                ('aktiv_elektr_energiya', models.FloatField()),
                ('reaktiv_elektr_energiya', models.FloatField()),
                ('qtm_energiya', models.FloatField()),
                ('suv_oqimi', models.FloatField()),
                ('trubina_suv_sarfi', models.FloatField()),
                ('salt_suv_sarfi', models.FloatField()),
                ('suv_omboridagi_suv_hajmi', models.FloatField()),
                ('xususiy_elektr_energiya', models.FloatField()),
                ('benzin', models.FloatField()),
                ('dizel', models.FloatField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]