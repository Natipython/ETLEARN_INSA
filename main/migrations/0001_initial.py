# Generated by Django 5.0.6 on 2024-06-26 21:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=225)),
                ('course_desc', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_title', models.CharField(max_length=225)),
                ('lesson_description', models.TextField()),
                ('lesson_content', models.TextField()),
                ('lesson_duration', models.DurationField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.lesson'),
        ),
    ]
