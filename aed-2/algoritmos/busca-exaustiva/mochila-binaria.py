# Implementar a solução do problema mochila 0-1 (0-1 knapsack problem usando busca exaustiva. 

def knapsack_exhaustive(items, capacity):
    n = len(items)
    max_value = 0
    best_combination = []

    # todas as combinações possíveis de itens (2^n combinações)
    for i in range(2 ** n):
        current_weight = 0
        current_value = 0
        combination = []

        for j in range(n):
            # se o j de i estiver definido, incluir o j item
            if i & (1 << j):
                current_weight += items[j][0]
                current_value += items[j][1]
                combination.append(j)

        # se a combinação atual é a melhor até agora
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            best_combination = combination

    return max_value, best_combination

items = [ # peso, valor
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 8)
]
capacity = 5

max_value, best_combination = knapsack_exhaustive(items, capacity)
print(f"Valor máximo: {max_value}")
print(f"Melhor combinação de itens: {best_combination}")