# Generated by Django 4.2.1 on 2023-06-08 15:47

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0021_remove_billing_student_student_billing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='billing',
            field=models.OneToOneField(null=True, on_delete=django.db.models.fields.CharField, to='authentication.billing'),
        ),
    ]