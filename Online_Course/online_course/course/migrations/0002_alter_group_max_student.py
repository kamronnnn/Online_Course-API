# Generated by Django 5.1.2 on 2024-10-13 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='max_student',
            field=models.IntegerField(default=0, help_text="O'quvchilar soni", verbose_name="O'quvchilar soni"),
        ),
    ]
