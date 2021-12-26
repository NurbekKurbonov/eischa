# Generated by Django 4.0 on 2021-12-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondadmin', '0006_tuman'),
    ]

    operations = [
        migrations.CreateModel(
            name='IFTUM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bolim', models.CharField(max_length=2, verbose_name='Bo`lim')),
                ('bob', models.IntegerField(verbose_name='Bob')),
                ('guruh', models.IntegerField(verbose_name='Guruh')),
                ('sinf', models.IntegerField(verbose_name='Sinf')),
                ('tartib', models.IntegerField(verbose_name='Tartib')),
                ('nomi', models.TextField(blank=True, unique=True, verbose_name='IFTUM nomi')),
            ],
            options={
                'verbose_name_plural': '01_IFTUM kodi',
            },
        ),
        migrations.AlterModelOptions(
            name='davlatlar',
            options={'verbose_name_plural': '01_Davlatlar'},
        ),
        migrations.AlterModelOptions(
            name='tuman',
            options={'verbose_name_plural': '03_Tumanlar'},
        ),
        migrations.AlterModelOptions(
            name='viloyat',
            options={'verbose_name_plural': '02_Viloyatlar'},
        ),
        migrations.AlterField(
            model_name='tuman',
            name='tuman_davlati',
            field=models.CharField(max_length=100, verbose_name='Tuman/shahar joylashgan davlat'),
        ),
        migrations.AlterField(
            model_name='tuman',
            name='tuman_kodi',
            field=models.IntegerField(verbose_name='Tuman/shahar kodi'),
        ),
        migrations.AlterField(
            model_name='tuman',
            name='tuman_nomi',
            field=models.CharField(max_length=100, verbose_name='Tuman/shahar nomi'),
        ),
        migrations.AlterField(
            model_name='tuman',
            name='tuman_viloyati',
            field=models.CharField(max_length=100, verbose_name='Tuman/shahar joylashgan viloyat'),
        ),
    ]