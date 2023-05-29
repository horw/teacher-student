import datetime

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager

languages_list = []
with open('./data/languages.txt', 'r') as file:
    languages_list = [(lan.strip(), lan.strip()) for lan in file.read().split('\n')]


class PersonInfo(models.Model):
    first_name = models.CharField("Фамилия", null=False)
    second_name = models.CharField("Имя", null=False)
    father_name = models.CharField("Отчество", null=False)

    number_of_contract = models.CharField("Номер Договора", null=True)
    passport_serial_with_number = models.CharField("Серия и номер паспорта", null=True)
    study_major = models.CharField("Направление обучения", null=True)
    region = models.CharField("Регион", null=True)
    school = models.CharField("Школа", null=True)

    LANG_CHOICES = languages_list
    language = models.CharField(
        choices=LANG_CHOICES,
        null=True
    )

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.second_name, self.father_name)

    class Meta(object):
        verbose_name = 'Персональные данные'
        verbose_name_plural = 'Персональные данные'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    person_info = models.OneToOneField(PersonInfo, on_delete=models.CharField, null=True)

    def __str__(self):
        try:
            return "%s %s %s" % (
                self.person_info.first_name, self.person_info.second_name, self.person_info.father_name)
        except Exception as e:
            return "error"

    class Meta(object):
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Topic(models.Model):
    title = models.CharField("Название")
    description = models.TextField("Описание", blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="topics")

    def user_directory_path(instance, filename):
        return 'uploaded/topic/{0}/{1}'.format(
            int(datetime.datetime.now().timestamp()),
            filename)

    upload = models.FileField(upload_to=user_directory_path, null=True)

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Топик'
        verbose_name_plural = 'Топики'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teachers = models.ManyToManyField(Teacher, through='StudentTeacher')
    topics = models.ManyToManyField(Topic, through='StudentTopic', related_name='students')
    person_info = models.OneToOneField(PersonInfo, on_delete=models.CharField, null=True)

    def __str__(self):
        try:
            return "%s %s %s" % (
                self.person_info.first_name, self.person_info.second_name, self.person_info.father_name)
        except Exception as e:
            return "error"

    class Meta(object):
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class StudentTeacher(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='student'
    )

    class Meta(object):
        constraints = [
            models.UniqueConstraint(fields=['teacher', 'student'], name='teacher_student_idx'),
        ]


class StudentTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='student'
    )

    class Meta(object):
        constraints = [
            models.UniqueConstraint(fields=['topic', 'student'], name='topic_student_idx'),
        ]
        verbose_name = 'Студент-Топик Канал'
        verbose_name_plural = 'Студент-Топик Канал'

    def __str__(self):
        return "%s %s %s" % (
            self.topic.title, self.student.person_info.first_name, self.student.person_info.second_name)


class Message(models.Model):

    def user_directory_path(instance, filename):
        return 'uploaded/user_{0}/{1}/{2}'.format(
            instance.studenttopic.student.user.id,
            int(datetime.datetime.now().timestamp()),
            filename)

    title = models.CharField("Сообщение")
    upload = models.FileField(upload_to=user_directory_path, null=True)
    studenttopic = models.ForeignKey(StudentTopic, on_delete=models.CASCADE, related_name="messages")
