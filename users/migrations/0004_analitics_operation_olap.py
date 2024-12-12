# Generated by Django 5.1.3 on 2024-12-05 07:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_delete_analitics_delete_operation_olap"),
    ]

    operations = [
        migrations.CreateModel(
            name="Analitics",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                ("month_year", models.CharField(max_length=255)),
                (
                    "total_spending",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
                ),
                (
                    "total_impact_from_employees",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
                ),
                (
                    "total_impact_from_users",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Operation_Olap",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                (
                    "Money_Used",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
                ),
                ("Time_Completed", models.DateTimeField()),
                ("Operation_Type", models.CharField(max_length=255)),
                ("Time_started", models.DateTimeField()),
                (
                    "User_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.user"
                    ),
                ),
            ],
        ),
    ]
