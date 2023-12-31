# Generated by Django 4.1.4 on 2023-03-29 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brs', '0003_bus'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('bus_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brs.bus')),
                ('from_s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brs.start')),
                ('to_s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brs.stop')),
            ],
        ),
    ]
