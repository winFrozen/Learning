# Generated by Django 4.2.6 on 2023-12-16 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_popcourses_hour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experts1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('img', models.ImageField(upload_to='Experts/img')),
            ],
        ),
    ]