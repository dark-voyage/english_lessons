# Generated by Django 4.1 on 2022-09-22 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_lesson_description_lesson_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='views',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default=1, max_length=512, verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to='images/', verbose_name='image'),
            preserve_default=False,
        ),
    ]