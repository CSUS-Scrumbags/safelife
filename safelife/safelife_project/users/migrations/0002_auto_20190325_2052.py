# Generated by Django 2.1.7 on 2019-03-26 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='student',
        ),
        migrations.RemoveField(
            model_name='class',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='students',
            name='studentName',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='teacherName',
        ),
        migrations.AlterField(
            model_name='accounts',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='identity',
            field=models.PositiveSmallIntegerField(choices=[(1, 'admin'), (2, 'teacher'), (3, 'student')], default=2),
        ),
        migrations.DeleteModel(
            name='Class',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]
