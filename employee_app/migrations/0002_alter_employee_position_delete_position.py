# Generated by Django 4.1.2 on 2022-11-24 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="position",
            field=models.CharField(max_length=60),
        ),
        migrations.DeleteModel(name="Position",),
    ]