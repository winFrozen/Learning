# Generated by Django 4.2.6 on 2023-12-16 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_courses1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Popcourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('shaxs', models.CharField(max_length=100)),
                ('son', models.IntegerField()),
                ('img', models.ImageField(upload_to='Popcourses/img')),
            ],
        ),
    ]