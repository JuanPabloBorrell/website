# Generated by Django 3.2.3 on 2022-05-06 11:38

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Skills', '0006_alter_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=ckeditor.fields.RichTextField(max_length=200),
        ),
    ]
