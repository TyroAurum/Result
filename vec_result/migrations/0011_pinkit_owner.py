# Generated by Django 4.1.1 on 2022-09-11 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vec_result', '0010_alter_pinkit_register_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='pinkit',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pinkits', to=settings.AUTH_USER_MODEL),
        ),
    ]
