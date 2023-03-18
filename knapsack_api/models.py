# Define the database fields in models.py
from django.db import models


class KnapsackProblem(models.Model):
    items = models.JSONField()
    capacity = models.IntegerField()