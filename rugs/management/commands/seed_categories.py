from django.core.management.base import BaseCommand
from rugs.models import Category


DATA = [
    ("Bakhtiari Rugs", "bakhtiari", "Durable tribal rugs with bold geometric and garden-panel designs."),
    ("Baluch Rugs", "baluch", "Compact tribal rugs with dark dramatic colors and symbolic detail."),
    ("Quchan Rugs", "quchan", "Northeastern Persian rugs with Kurdish influence and bold geometry."),
    ("Hamadan Rugs", "hamadan", "Practical village carpets with strong medallions and excellent value."),
    ("Kashan Rugs", "kashan", "Elegant city carpets with refined floral medallions and luxury appeal."),
    ("Kerman Rugs", "kerman", "Artistic Persian carpets with graceful floral patterns and soft colors."),
    ("Lori Rugs", "lori", "Expressive tribal pieces with strong symbols and earthy colors."),
    ("Nahavand Rugs", "nahavand", "Village rugs with vibrant colors, diamond medallions and durability."),
    ("Shiraz Rugs", "shiraz", "Southern tribal rugs with animal motifs and rich nomadic spirit."),
    ("Tabriz Rugs", "tabriz", "Prestigious Persian masterpieces with fine detail and high knot density."),
    ("Sultanabad Rugs", "sultanabad", "Decorative Persian rugs with grand patterns and elegant village charm."),
    ("Turkmen Rugs", "turkmen", "Iconic red tribal rugs with repeating Gul motifs and strong identity."),
    ("Qom Rugs", "qom", "Luxurious Persian rugs known for silk, fine detail and prestige."),
]


class Command(BaseCommand):
    help = "Create starter rug categories."

    def handle(self, *args, **options):
        for order, (name, slug, short) in enumerate(DATA, start=1):
            Category.objects.update_or_create(
                slug=slug,
                defaults={
                    "name": name,
                    "short_description": short,
                    "description": f"Authentic {name} by Keshmiri Rugs. This collection is presented for clients who appreciate Persian heritage, handmade character and timeless decorative value.",
                    "design_character": "Authentic Persian craftsmanship\nHandwoven character\nTimeless decorative value",
                    "features": "Authentic Persian craftsmanship\nHandwoven character\nTimeless decorative value",
                    "why_choose": "A beautiful choice for collectors, interior designers and homeowners looking for authentic craftsmanship, visual warmth and cultural identity.",
                    "order": order,
                    "is_active": True,
                },
            )
        self.stdout.write(self.style.SUCCESS("Starter categories created/updated."))
