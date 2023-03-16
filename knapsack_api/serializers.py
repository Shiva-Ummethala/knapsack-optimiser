from rest_framework import serializers
from .models import KnapsackProblem


class KnapsackProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnapsackProblem
        fields = '__all__'