# Generated by Django 3.2.9 on 2021-11-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0005_auto_20211129_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
