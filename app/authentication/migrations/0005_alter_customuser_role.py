# Generated by Django 4.2.1 on 2023-05-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_customuser_email_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Учитель'), (2, 'Ученик')], null=True, verbose_name='Роль'),
        ),
    ]
