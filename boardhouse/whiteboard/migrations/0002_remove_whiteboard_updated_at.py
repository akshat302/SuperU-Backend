# Generated by Django 4.1.3 on 2023-08-20 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('whiteboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='whiteboard',
            name='updated_at',
        ),
    ]