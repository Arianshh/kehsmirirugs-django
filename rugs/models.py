from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    short_description = models.TextField(blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to="categories/", blank=True, null=True)
    design_character = models.TextField(
        blank=True,
        help_text="One item per line. Appears under Design Character on the category page.",
    )
    features = models.TextField(
        blank=True,
        help_text="One feature per line. These appear on the category detail page.",
    )
    why_choose = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


    @property
    def design_character_list(self):
        source = getattr(self, "design_character", "") or getattr(self, "features", "")
        return [line.strip() for line in source.splitlines() if line.strip()]

    @property
    def feature_list(self):
        return self.design_character_list
