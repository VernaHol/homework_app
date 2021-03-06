# Generated by Django 3.2.9 on 2021-12-02 14:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(default='', max_length=200)),
                ('teacher', models.CharField(default='', max_length=200)),
                ('semester', models.CharField(default='', max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment', models.CharField(default='', max_length=200)),
                ('deadline', models.DateTimeField()),
                ('materials', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(default=False)),
                ('course', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='homeworkapp.course')),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
