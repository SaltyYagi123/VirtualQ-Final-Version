# Generated by Django 4.1.3 on 2023-05-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clientApp", "0005_delete_ticket"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="height",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
