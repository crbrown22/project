# Generated by Django 4.1.3 on 2023-11-13 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(choices=[('T-shirt', 'T-shirt'), ('Hoodie', 'Hoodie'), ('Shorts', 'Shorts'), ('Joggers', 'Joggers'), ('Socks', 'Socks'), ('Supplements', 'Supplements'), ('Programs', 'Programs'), ('Subscription', 'Subscription')], max_length=20, null=True)),
                ('quantity', models.PositiveBigIntegerField(null=True)),
            ],
        ),
    ]