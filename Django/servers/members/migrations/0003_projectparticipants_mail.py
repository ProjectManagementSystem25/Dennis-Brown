# Generated by Django 5.1.5 on 2025-02-11 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_projectparticipants_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectparticipants',
            name='mail',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
