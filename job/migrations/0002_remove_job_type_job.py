# Generated by Django 3.2 on 2023-03-03 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='type_job',
        ),
    ]
