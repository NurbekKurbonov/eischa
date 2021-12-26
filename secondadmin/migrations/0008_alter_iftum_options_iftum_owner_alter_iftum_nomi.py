# Generated by Django 4.0 on 2021-12-25 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('secondadmin', '0007_iftum_alter_davlatlar_options_alter_tuman_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iftum',
            options={'verbose_name_plural': '04_IFTUM kodi'},
        ),
        migrations.AddField(
            model_name='iftum',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='iftum',
            name='nomi',
            field=models.CharField(max_length=500, unique=True, verbose_name='IFTUM nomi'),
        ),
    ]