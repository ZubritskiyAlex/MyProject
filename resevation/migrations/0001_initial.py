from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teespring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('phone', models.DateTimeField(max_length=50, verbose_name='phone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teespring.product', verbose_name='product')),
            ],
        ),
    ]