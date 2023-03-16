
# knapsack_api/models.py
from django.db import models


class KnapsackProblem(models.Model):
    items = models.JSONField()
    capacity = models.IntegerField()