# Generated by Django 4.0.1 on 2022-03-08 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userlogin', '0003_image_facedata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='Department',
        ),
    ]