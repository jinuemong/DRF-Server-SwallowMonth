# Generated by Django 4.1.6 on 2023-03-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fuser',
            name='otherUser',
            field=models.CharField(default=False, max_length=20),
        ),
    ]
