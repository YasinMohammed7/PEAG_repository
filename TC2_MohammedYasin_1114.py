import random

def fitness(p):
    n = len(p)
    total_pairs = n * (n - 1) // 2
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(p[i] - p[j]) == abs(i - j):
                conflicts += 1
    return total_pairs - conflicts

def generate_population(n, dim):
    pop = []
    for _ in range(dim):
        individual = random.sample(range(1, n+1), n)
        fit = fitness(individual)
        individual_with_fitness = individual + [fit]
        pop.append(individual_with_fitness)
    return pop

# def has_duplicates(pop):
#     seen = set()
#     for ind in pop:
#         t = tuple(ind)
#         if t in seen:
#             print(f"Duplicate found: {ind}")
#             return True
#         seen.add(t)
#     return False

if __name__ == '__main__':
    n = 8
    dim = 28
    print(generate_population(n, dim))
    # popArr = generate_population(n, dim)
    # if has_duplicates(popArr):
    #     print("Population contains duplicates.")
    # else:
    #     print("All individuals are unique.")