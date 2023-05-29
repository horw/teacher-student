from django.contrib import admin

# Register your models here.
from .models import Student, Teacher, PersonInfo, StudentTeacher, Topic, StudentTopic, Message


class StudentTeacherInline(admin.TabularInline):
    model = StudentTeacher


class StudentTopicInline(admin.TabularInline):
    model = StudentTopic


class TopicInline(admin.TabularInline):
    model = Topic


class MessageInline(admin.TabularInline):
    model = Message


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = (StudentTeacherInline, StudentTopicInline)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = (StudentTeacherInline, TopicInline)


@admin.register(PersonInfo)
class PersonInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass


@admin.register(StudentTopic)
class StudentTopicAdmin(admin.ModelAdmin):
    inlines = (MessageInline,)
