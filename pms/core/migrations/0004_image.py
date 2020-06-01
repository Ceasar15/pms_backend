# Generated by Django 3.0.6 on 2020-05-23 11:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_drug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('file', models.ImageField(upload_to='images')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]