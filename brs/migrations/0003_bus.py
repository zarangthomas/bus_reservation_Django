# Generated by Django 4.1.4 on 2023-03-29 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brs', '0002_start_stop_delete_places'),
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_name', models.CharField(max_length=20)),
                ('from_s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brs.start')),
                ('to_s', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brs.stop')),
            ],
        ),
    ]
