def Knapsack(weights, values, max_weight):
    n = len(weights)
    x = [0] * n
    weight = 0
    while weight < max_weight:
        i = BestItem(weights, values, x)
        if weight + weights[i] <= max_weight:
            x[i] = 1
            weight += weights[i]
        else:
            x[i] = (max_weight - weight) / weights[i]
            weight = max_weight
    return x

def BestItem(weights, values, x):
    max_value_per_weight = 0
    best_item_index = -1
    for i in range(len(weights)):
        if x[i] == 0 and weights[i] > 0:
            value_per_weight = values[i] / weights[i]
            if value_per_weight > max_value_per_weight:
                max_value_per_weight = value_per_weight
                best_item_index = i
    return best_item_index

weights = [10, 20, 30, 40, 50]
values = [20, 30, 66, 40, 60]
max_weight = 100
print(Knapsack(weights, values, max_weight))