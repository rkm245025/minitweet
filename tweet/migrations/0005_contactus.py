# Generated by Django 4.2.6 on 2024-07-13 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0004_delete_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('info', models.CharField(max_length=1000)),
                ('email', models.TextField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('date_added', models.DateField(auto_now=True)),
            ],
        ),
    ]
