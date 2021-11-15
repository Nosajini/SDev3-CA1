# Generated by Django 3.2.9 on 2021-11-15 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='body',
            field=models.TextField(default='Hello!', max_length=500),
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profilepic/'),
        ),
    ]
