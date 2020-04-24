# Generated by Django 3.0.4 on 2020-03-17 17:45

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('users', models.ManyToManyField(related_name='branches', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
