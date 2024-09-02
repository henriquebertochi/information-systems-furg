# Implementar a solução do problema distribuição de tarefas (assignment problem) usando busca exaustiva.

def generate_permutations(tasks):
    if len(tasks) == 0:
        return [[]]
    
    permutations = []
    for i in range(len(tasks)):
        current_task = tasks[i]
        remaining_tasks = tasks[:i] + tasks[i+1:]
        for p in generate_permutations(remaining_tasks):
            permutations.append([current_task] + p)
    
    return permutations

def assignment_problem(cost_matrix):
    num_tasks = len(cost_matrix[0])

    permutations = generate_permutations(list(range(num_tasks)))
    min_cost = float('inf')
    best_assignment = None

    for assignment in permutations:
        current_cost = 0
        for worker, task in enumerate(assignment):
            current_cost += cost_matrix[worker][task]

        if current_cost < min_cost:
            min_cost = current_cost
            best_assignment = assignment

    return min_cost, best_assignment

cost_matrix = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]

min_cost, best_assignment = assignment_problem(cost_matrix)
print(f"Minimum cost: {min_cost}")
print(f"Best assignment: {best_assignment}")