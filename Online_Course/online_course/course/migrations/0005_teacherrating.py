# Generated by Django 5.1.2 on 2024-10-13 20:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_averagerating_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(help_text='Baxosi', max_length=3, verbose_name='Baxosi')),
                ('added', models.DateTimeField(auto_now_add=True, help_text='Baxo berilgan vaxt', verbose_name='Baxo berilgan vaxt')),
                ('updated', models.DateTimeField(auto_now_add=True, help_text='Baxo yangilangan vaxt', verbose_name='Baxo yangilangan vaxt')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.teacher')),
            ],
        ),
    ]
