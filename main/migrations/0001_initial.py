# Generated by Django 5.0.6 on 2024-06-07 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='фамилия')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='students/', verbose_name='аватар')),
            ],
            options={
                'verbose_name': 'студент',
                'verbose_name_plural': 'студенты',
                'ordering': ('last_name',),
            },
        ),
    ]
