# Generated by Django 2.0.2 on 2020-01-03 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_remove_fileupload_file_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='file_type',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]
