"""CRUD app Models"""

# Utils
import uuid
import random

# Django
from django.db import models


def random_list():
    return random.sample(range(1, 100), 50)


class Company(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(
        max_length=50,
        help_text="Name",
        null=False,
        blank=False
    )
    description = models.CharField(
        max_length=100,
        help_text="Description"
    )
    symbol = models.CharField(
        max_length=10,
        help_text="Symbol"
    )
    market_values = models.TextField(
        default=random_list
    )

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return f"{self.name} - {self.symbol}"
