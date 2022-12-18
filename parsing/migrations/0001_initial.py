# Generated by Django 4.1.3 on 2022-12-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="")),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200, verbose_name="TITLE")),
                ("director", models.CharField(max_length=50, verbose_name="DIRECTOR")),
                ("image", models.ImageField(upload_to="", verbose_name="IMAGE")),
                ("point", models.FloatField(verbose_name="POINT")),
                ("cast", models.ManyToManyField(blank=True, to="parsing.actor")),
            ],
        ),
    ]
