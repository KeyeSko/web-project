from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Anecdot(models.Model):

    class AnecCategory(models.TextChoices):
        Fam = "Family", "FAMILY"
        Army = "Army", "ARMY"
        Other = "Other", "OTHER"

    text = models.TextField()
    like_count = models.IntegerField(default='0')
    category = models.CharField(max_length=10, choices=AnecCategory.choices, default='Other')
