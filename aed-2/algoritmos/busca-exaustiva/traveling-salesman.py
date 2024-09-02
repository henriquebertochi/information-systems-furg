# Implementar a solução do problemas do caixeiro viajante (traveling salesman problem) usando busca exaustiva.

def generate_permutations(elements):
    if len(elements) == 0:
        return [[]]

    permutations = []
    for i in range(len(elements)):
        current_element = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        for p in generate_permutations(remaining_elements):
            permutations.append([current_element] + p)

    return permutations


def traveling_salesman(distance_matrix):
    num_cities = len(distance_matrix)

    # gerar todas as permutações possíveis das cidades, mas exlui a cidade (0) de partida
    cities = list(range(1, num_cities))
    permutations = generate_permutations(cities)

    min_distance = float('inf')
    best_route = None

    for perm in permutations:
        current_distance = 0
        current_route = [0] + perm + [0]  # cidade de partida e retorno

        # distância total da rota atual
        for i in range(len(current_route) - 1):
            current_distance += distance_matrix[current_route[i]
                                                ][current_route[i+1]]

        # atualizar menor distância e a melhor rota
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = current_route

    return min_distance, best_route


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_distance, best_route = traveling_salesman(distance_matrix)
print(f"Menor distância: {min_distance}")
print(f"Melhor rota: {best_route}")