# Generated by Django 4.2.1 on 2023-05-28 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_alter_message_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studenttopic',
            options={'verbose_name': 'Студент-Топик Канал', 'verbose_name_plural': 'Студент-Топик Канал'},
        ),
        migrations.RemoveField(
            model_name='message',
            name='teacher',
        ),
    ]
