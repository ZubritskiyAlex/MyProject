# Generated by Django 3.2.4 on 2021-06-12 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teespring', '0011_store_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teespring.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
