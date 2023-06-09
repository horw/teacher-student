# Generated by Django 4.2.1 on 2023-05-28 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_customuser_father_name_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail адрес'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Teacher'), (2, 'Student')], null=True, verbose_name='Роль'),
        ),
    ]
