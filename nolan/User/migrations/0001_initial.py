# Generated by Django 4.2.3 on 2023-07-12 08:49

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Scripts",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("scenes", models.JSONField()),
                ("characters", models.JSONField()),
                ("pdf_format", models.FileField(upload_to="scripts/")),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("scripts", models.ManyToManyField(to="User.scripts")),
            ],
        ),
    ]
