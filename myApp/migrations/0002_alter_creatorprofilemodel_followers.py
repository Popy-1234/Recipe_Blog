# Generated by Django 5.1 on 2024-10-29 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatorprofilemodel',
            name='followers',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
