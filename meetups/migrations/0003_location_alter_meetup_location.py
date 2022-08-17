# Generated by Django 4.0.4 on 2022-08-16 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_meetup_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='meetup',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetups.location'),
        ),
    ]
