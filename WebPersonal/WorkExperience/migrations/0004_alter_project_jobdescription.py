# Generated by Django 3.2.9 on 2021-11-30 08:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkExperience', '0003_auto_20211130_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='jobdescription',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
