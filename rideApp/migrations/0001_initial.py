# Generated by Django 4.1.3 on 2023-05-19 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ThemePark",
            fields=[
                ("park_id", models.AutoField(primary_key=True, serialize=False)),
                ("park_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="ThemeParkArea",
            fields=[
                ("area_id", models.AutoField(primary_key=True, serialize=False)),
                ("area_name", models.CharField(max_length=255)),
                (
                    "park_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rideApp.themepark",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ThemeParkRide",
            fields=[
                ("ride_id", models.AutoField(primary_key=True, serialize=False)),
                ("ride_name", models.CharField(max_length=255)),
                ("ride_description", models.TextField()),
                (
                    "ride_thumbnail",
                    models.ImageField(upload_to="media/ride_thumbnails/"),
                ),
                ("height_restriction", models.PositiveIntegerField()),
                ("ride_capacity", models.PositiveIntegerField()),
                ("ride_duration", models.PositiveIntegerField()),
                ("opening_hour", models.TimeField()),
                ("closing_hour", models.TimeField()),
                ("under_maintenance", models.BooleanField()),
                ("accessibility_wheelchair_access", models.BooleanField(default=False)),
                ("accessibility_audio_description", models.BooleanField(default=False)),
                ("accessibility_braille", models.BooleanField(default=False)),
                ("accessibility_sign_language", models.BooleanField(default=False)),
                ("accessibility_closed_captioning", models.BooleanField(default=False)),
                ("accessibility_tactile_path", models.BooleanField(default=False)),
                ("accessibility_other", models.BooleanField(default=False)),
                (
                    "ride_type",
                    models.CharField(
                        choices=[
                            ("ROLLER_COASTER", "Roller Coaster"),
                            ("BIG_DROPS", "Big Drops"),
                            ("SMALL_DROPS", "Small Drops"),
                            ("THRILL_RIDES", "Thrill Rides"),
                            ("SLOW_RIDES", "Slow Rides"),
                            ("STAGE_SHOWS", "Stage Shows"),
                            ("FIREWORKS", "Fireworks"),
                            ("CHARACTER_EXPERIENCES", "Character Experience"),
                            ("PARADES", "Parades"),
                            ("WATER_RIDES", "Water Rides"),
                            ("SPINNING", "Spinning"),
                            ("LIVE", "Live Entertainment"),
                            ("DARK", "Dark"),
                            ("LOUD", "Loud"),
                            ("SCARY", "Scary"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "age_restriction",
                    models.CharField(
                        choices=[
                            ("PREESCHOOLERS", "Preeschoolers"),
                            ("KIDS", "Kids"),
                            ("TEENS", "Teens"),
                            ("ADULTS", "Adults"),
                            ("TWEENS", "Tweens"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "area_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rideApp.themeparkarea",
                    ),
                ),
                (
                    "park_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rideApp.themepark",
                    ),
                ),
            ],
        ),
    ]
