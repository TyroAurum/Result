# Generated by Django 4.1.1 on 2022-09-12 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vec_result', '0011_pinkit_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pinkit',
            name='owner',
        ),
    ]
