# knapsack_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import KnapsackProblemSerializer
from .knapsack import knapsack


class KnapsackOptimizer(APIView):
    def post(self, request):
        serializer = KnapsackProblemSerializer(data=request.data)
        if serializer.is_valid():
            knapsack_problem = serializer.save()
            result = knapsack(knapsack_problem.items, knapsack_problem.capacity)
            return Response({
                'result': result[0],
                'items': result[1]
            })
        else:
            return Response(serializer.errors, status=400)
