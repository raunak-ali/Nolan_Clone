# Generated by Django 4.2.3 on 2023-07-16 15:52

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):
    dependencies = [
        ("User", "0004_userprofile_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="scripts",
            name="genres",
            field=multiselectfield.db.fields.MultiSelectField(
                choices=[
                    ("sci-fi", "Science Fiction"),
                    ("horror", "Horror"),
                    ("fantasy", "Fantasy"),
                    ("romance", "Romance"),
                ],
                default="horror",
                max_length=50,
            ),
            preserve_default=False,
        ),
    ]
