# Generated by Django 2.2.15 on 2020-08-24 05:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='investors',
        ),
        migrations.AddField(
            model_name='project',
            name='needed_money',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_invested', models.IntegerField()),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investments', to='app.Project')),
            ],
        ),
    ]
