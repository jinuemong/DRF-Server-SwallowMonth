# Generated by Django 4.0.3 on 2023-01-19 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthData',
            fields=[
                ('monthId', models.BigAutoField(help_text='month ID', primary_key=True, serialize=False)),
                ('keyDate', models.CharField(default=False, max_length=20)),
                ('totalPer', models.IntegerField()),
                ('totalPoint', models.IntegerField()),
                ('doneTask', models.IntegerField()),
                ('clearRoutine', models.IntegerField()),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthPost', to=settings.AUTH_USER_MODEL, to_field='userName')),
            ],
        ),
    ]
