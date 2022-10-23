from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator

class Thing(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False
    )
    description = models.TextField(
        unique=False,
        blank=True, 
        validators=[MaxLengthValidator(120)]
    )
    quantity = models.IntegerField(
        unique=False,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
            ]
    )
