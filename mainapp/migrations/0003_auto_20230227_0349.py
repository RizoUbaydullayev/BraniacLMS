# Generated by Django 3.2.16 on 2023-02-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_data_migratin"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="lesson",
            name="cost",
        ),
        migrations.RemoveField(
            model_name="lesson",
            name="cover",
        ),
        migrations.AlterField(
            model_name="lesson",
            name="num",
            field=models.PositiveIntegerField(verbose_name="Lesson number"),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="title",
            field=models.CharField(max_length=256, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="news",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
    ]
