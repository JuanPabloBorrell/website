# Generated by Django 3.2.3 on 2022-05-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0007_alter_project_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.SmallIntegerField(default=0),
        ),
    ]
