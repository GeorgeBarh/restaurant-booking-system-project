from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    class Meta:
        ordering = ["table_number"]

    def __str__(self):
        return f"Table {self.table_number} (Seats {self.capacity})"


class Booking(models.Model):
    STATUS_CHOICES = (
        (0, "Pending"),
        (1, "Confirmed"),
        (2, "Cancelled"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ["date", "time"]

    def __str__(self):
        return f"{self.user} - {self.date} at {self.time}"


class MenuItem(models.Model):
    STATUS = (
        (0, "Unavailable"),
        (1, "Available"),
    )

    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
