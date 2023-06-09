# Generated by Django 4.2.1 on 2023-05-28 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_studentteacher_student_teachers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personinfo',
            options={'verbose_name': 'Персональные данные', 'verbose_name_plural': 'Персональные данные'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Учитель', 'verbose_name_plural': 'Учителя'},
        ),
        migrations.AlterField(
            model_name='personinfo',
            name='father_name',
            field=models.CharField(verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='personinfo',
            name='first_name',
            field=models.CharField(verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='personinfo',
            name='second_name',
            field=models.CharField(verbose_name='Имя'),
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Название')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.teacher')),
            ],
            options={
                'verbose_name': 'Топик',
                'verbose_name_plural': 'Топики',
            },
        ),
    ]
