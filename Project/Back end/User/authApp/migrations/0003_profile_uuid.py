# Generated by Django 3.0.5 on 2021-05-23 10:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_profile_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
