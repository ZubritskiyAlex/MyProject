# Generated by Django 3.2.4 on 2021-06-04 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teespring', '0003_auto_20210604_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=30, verbose_name='username'),
        ),
    ]
