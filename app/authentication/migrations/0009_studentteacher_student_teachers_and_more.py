# Generated by Django 4.2.1 on 2023-05-28 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_remove_student_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.student', verbose_name='student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teachers',
            field=models.ManyToManyField(through='authentication.StudentTeacher', to='authentication.teacher'),
        ),
        migrations.AddConstraint(
            model_name='studentteacher',
            constraint=models.UniqueConstraint(fields=('teacher', 'student'), name='teacher_student_idx'),
        ),
    ]