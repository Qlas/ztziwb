from django.contrib.auth.models import User
from django.db import models


class ContactForm(models.Model):
    user = models.ForeignKey(User, related_name="results", on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField()
    topic = models.CharField(max_length=512, blank=True)
    purpose = models.CharField(max_length=512, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user, self.temat}"
