# Generated by Django 5.1.1 on 2024-09-13 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
