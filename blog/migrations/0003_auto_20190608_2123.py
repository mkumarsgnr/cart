# Generated by Django 2.2.1 on 2019-06-08 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190608_1734'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='post_id_id',
            new_name='post_id',
        ),
    ]
