# Generated by Django 4.2.6 on 2023-12-16 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_popcourses_hour'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='popcourses',
            name='hour',
        ),
    ]
