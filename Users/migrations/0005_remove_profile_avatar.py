# Generated by Django 4.2.2 on 2023-07-14 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
    ]
