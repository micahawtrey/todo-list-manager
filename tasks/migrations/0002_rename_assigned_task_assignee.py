# Generated by Django 5.0 on 2023-12-19 19:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="assigned",
            new_name="assignee",
        ),
    ]
