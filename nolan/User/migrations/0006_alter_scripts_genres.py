# Generated by Django 4.2.3 on 2023-07-16 17:04

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0005_scripts_genres"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scripts",
            name="genres",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("sci-fi", "Science Fiction"),
                    ("horror", "Horror"),
                    ("fantasy", "Fantasy"),
                    ("romance", "Romance"),
                ],
                max_length=1000,
            ),
        ),
    ]
