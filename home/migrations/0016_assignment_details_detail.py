# Generated by Django 3.2.8 on 2021-12-01 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20211201_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment_details',
            name='detail',
            field=models.CharField(default='', max_length=100),
        ),
    ]