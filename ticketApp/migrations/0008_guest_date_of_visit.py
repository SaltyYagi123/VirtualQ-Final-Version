# Generated by Django 4.1.3 on 2023-05-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticketApp", "0007_alter_guest_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="guest",
            name="date_of_visit",
            field=models.DateField(null=True),
        ),
    ]
