from django.db import models

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ("starter", "Starter"),
        ("main", "Main Course"),
        ("dessert", "Dessert"),
        ("drink", "Drink"),
        ("vegan", "Vegan"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.IntegerField(choices=[(0, "Unavailable"), (1, "Available")], default=1)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="main")
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
