# knapsack_optimizer/urls.py
from django.urls import path
from knapsack_api.views import KnapsackOptimizer


urlpatterns = [
    path('knapsack/', KnapsackOptimizer.as_view(), name='knapsack_optimizer'),
]
