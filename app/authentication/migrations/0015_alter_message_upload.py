# Generated by Django 4.2.1 on 2023-05-28 18:44

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_message_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='upload',
            field=models.FileField(null=True, upload_to=authentication.models.Message.user_directory_path),
        ),
    ]
