# knapsack algorithm using matrix approach
def knapsack(items, capacity):
    # initialize a matrix of zeros with dimensions (items + 1) x (capacity + 1)
    matrix = [[0 for x in range(capacity + 1)] for x in range(len(items) + 1)]

    # iterate over the items
    for i in range(1, len(items) + 1):
        weight, value = items[i-1]
        # iterate over the capacity values from 0 to capacity
        for j in range(capacity + 1):
            if weight > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-weight] + value)

    # backtracking to get the items
    items_selected = []
    i = len(items)
    j = capacity
    while i > 0 and j > 0:
        if matrix[i][j] != matrix[i-1][j]:
            items_selected.append(items[i-1])
            j -= items[i-1][0]
        i -= 1

    return matrix[-1][-1], items_selected[::-1]
