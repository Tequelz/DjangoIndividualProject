# Generated by Django 3.2 on 2021-04-30 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_api', '0003_teachingsession_unique_sign_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lec_number', models.IntegerField()),
                ('lec_length', models.IntegerField()),
                ('lec_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('mod_name', models.CharField(max_length=100)),
                ('mod_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='lessonid',
            name='lec_teacher',
        ),
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.RemoveConstraint(
            model_name='lecturesession',
            name='unique_sign_in',
        ),
        migrations.RemoveField(
            model_name='lecturesession',
            name='lesson_id',
        ),
        migrations.AddConstraint(
            model_name='lecturesession',
            constraint=models.UniqueConstraint(fields=('username', 'lecture_id'), name='unique_sign_in'),
        ),
        migrations.RenameModel(
            old_name='TeachingSession',
            new_name='LectureSession',
        ),
        migrations.DeleteModel(
            name='LessonID',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='module',
            name='mod_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='lecture',
            name='lec_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_api.module'),
        ),
        migrations.AddField(
            model_name='lecturesession',
            name='lecture_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_api.lecture'),
        ),
    ]
