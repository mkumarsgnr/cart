# Generated by Django 2.2.1 on 2019-05-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190517_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.IntegerField(default='')),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
