# Generated by Django 4.1.3 on 2023-11-17 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='ksp.jpg', upload_to='profile_images'),
        ),
    ]