# Generated by Django 4.2.5 on 2023-10-03 02:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="section",
            old_name="parent_section",
            new_name="parent",
        ),
    ]