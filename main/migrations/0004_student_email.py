# Generated by Django 5.0.6 on 2024-07-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, verbose_name='email'),
        ),
    ]
