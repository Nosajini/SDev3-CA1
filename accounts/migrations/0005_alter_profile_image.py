# Generated by Django 3.2.9 on 2021-11-15 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211115_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='profilepic/default_profile.jpg/', upload_to='profilepic/'),
        ),
    ]