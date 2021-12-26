# Generated by Django 4.0 on 2021-12-19 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('ges', '0009_alter_v_parameters_sana'),
    ]

    operations = [
        migrations.AlterField(
            model_name='v_parameters',
            name='sana',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='new_periodical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hisobot_nomi', models.CharField(max_length=266)),
                ('hisobot_sanasi', models.DateField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]