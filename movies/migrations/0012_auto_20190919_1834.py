# Generated by Django 2.2.5 on 2019-09-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20190919_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='website',
            field=models.CharField(blank=True, max_length=50, verbose_name='Website'),
        ),
    ]
