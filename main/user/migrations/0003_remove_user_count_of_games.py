# Generated by Django 5.1.6 on 2025-02-17 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_count_of_games'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='count_of_games',
        ),
    ]
