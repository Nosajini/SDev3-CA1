# Generated by Django 3.2.9 on 2021-11-13 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='location',
            field=models.TextField(blank=True, default='n/a', max_length=30),
        ),
    ]