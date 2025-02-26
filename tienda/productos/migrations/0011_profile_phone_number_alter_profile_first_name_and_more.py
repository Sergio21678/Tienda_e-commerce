# Generated by Django 5.1.2 on 2024-11-05 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0010_rename_apellido_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
