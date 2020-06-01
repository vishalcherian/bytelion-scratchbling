# Generated by Django 3.0.6 on 2020-05-31 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_size', models.CharField(max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='item_size',
        ),
    ]
