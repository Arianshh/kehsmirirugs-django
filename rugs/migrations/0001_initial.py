# Generated manually for Keshmiri Rugs

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=120)),
                ("slug", models.SlugField(unique=True)),
                ("short_description", models.TextField(blank=True)),
                ("description", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="categories/")),
                ("features", models.TextField(blank=True, help_text="One feature per line. These appear on the category detail page.")),
                ("why_choose", models.TextField(blank=True)),
                ("order", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name_plural": "Categories",
                "ordering": ["order", "name"],
            },
        ),
    ]
