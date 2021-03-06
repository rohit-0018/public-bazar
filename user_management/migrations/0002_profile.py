# Generated by Django 2.1 on 2019-02-13 07:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_first_name', models.CharField(max_length=30)),
                ('p_middle_name', models.CharField(blank=True, max_length=30)),
                ('p_last_name', models.CharField(blank=True, max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('profile_pic', models.ImageField(blank=True, upload_to='')),
                ('cover_pic', models.ImageField(blank=True, upload_to='')),
                ('date_of_birth', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
