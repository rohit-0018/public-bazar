# Generated by Django 2.1 on 2019-02-13 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='p_first_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='p_last_name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='p_middle_name',
            new_name='middle_name',
        ),
    ]