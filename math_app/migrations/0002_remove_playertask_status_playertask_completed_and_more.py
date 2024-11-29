# Generated by Django 5.1.3 on 2024-11-14 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playertask',
            name='status',
        ),
        migrations.AddField(
            model_name='playertask',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=63),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=63),
        ),
    ]
