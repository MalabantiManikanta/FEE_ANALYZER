# Generated by Django 4.2.4 on 2023-09-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlapp', '0002_students_delete_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
