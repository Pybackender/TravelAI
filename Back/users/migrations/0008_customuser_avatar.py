# Generated by Django 5.1 on 2024-10-18 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_remove_customuser_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="avatar",
            field=models.FileField(blank=True, null=True, upload_to=""),
        ),
    ]
