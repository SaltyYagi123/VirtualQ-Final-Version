# Generated by Django 4.1.3 on 2023-05-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("queueApp", "0003_remove_ridereservation_id_remove_rideschedule_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ridereservation",
            name="reservation_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="rideschedule",
            name="schedule_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]