# Generated by Django 4.1.3 on 2023-05-22 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ticketApp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ticket",
            name="additional_guests",
        ),
        migrations.AddField(
            model_name="ticket",
            name="additional_guests_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="ticket",
            name="guest_number",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
