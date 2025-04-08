from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Table model
class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.table_number} (Seats: {self.capacity})"
