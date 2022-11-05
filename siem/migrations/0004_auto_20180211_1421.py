# Generated by Django 2.0.1 on 2018-02-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siem', '0003_auto_20180209_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logevent',
            old_name='username',
            new_name='target_user',
        ),
        migrations.AddField(
            model_name='logevent',
            name='source_user',
            field=models.CharField(default='', max_length=32),
        ),
    ]
