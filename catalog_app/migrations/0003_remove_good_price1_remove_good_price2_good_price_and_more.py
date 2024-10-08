# Generated by Django 4.2 on 2024-09-01 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0002_alter_good_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='price1',
        ),
        migrations.RemoveField(
            model_name='good',
            name='price2',
        ),
        migrations.AddField(
            model_name='good',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=15, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='good',
            name='art',
            field=models.CharField(blank=True, db_index=True, default='', max_length=50, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='good',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1024, verbose_name='Описание'),
        ),
    ]
