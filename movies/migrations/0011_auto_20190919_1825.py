# Generated by Django 2.2.5 on 2019-09-19 18:25

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_auto_20190919_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='ratings',
            field=jsonfield.fields.JSONField(blank=True),
        ),
    ]
