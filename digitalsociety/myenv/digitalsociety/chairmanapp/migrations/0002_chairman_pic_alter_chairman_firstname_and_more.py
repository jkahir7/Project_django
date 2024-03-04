# Generated by Django 5.0 on 2024-01-06 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chairmanapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chairman',
            name='pic',
            field=models.FileField(default='default.jpeg', upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='chairman',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chairman',
            name='houseno',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='chairman',
            name='lastname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='chairman',
            name='userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chairmanapp.user'),
        ),
    ]
