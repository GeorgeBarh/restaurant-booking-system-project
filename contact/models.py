from django.db import models

# Contact message model to store form submissions
class ContactMessage(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

