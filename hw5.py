import random

def genetic_algorithm(population, fitness_function, target_fitness, max_generations=1000):
    generation = 0

    while generation < max_generations:
        population_fitness = [fitness_function(individual) for individual in population]
        weights = weighted_by(population_fitness)
        population2 = []

        for _ in range(len(population)):
            parent1, parent2 = weighted_random_choices(population, weights, 2)
            child = reproduce(parent1, parent2)
            mutation_probability = random.uniform(0, 0.05)  # Random value between 0 and 0.05
            if random.random() < mutation_probability:
                child = mutate(child)

            population2.append(child)

        population = population2
        best_individual = max(population, key=fitness_function)
        if fitness_function(best_individual) >= target_fitness:
            return best_individual

        generation += 1

    return max(population, key=fitness_function)

def reproduce(parent1, parent2):
    n = len(parent1)
    c = random.randint(1, n - 1)
    return parent1[:c] + parent2[c:]

def weighted_by(fitness_scores):
    total_fitness = sum(fitness_scores)
    weights = [score / total_fitness for score in fitness_scores]
    return weights

def weighted_random_choices(population, weights, num_choices):
    return random.choices(population, weights=weights, k=num_choices)

def mutate(child):
    mutation_point = random.randint(0, len(child) - 1)
    child[mutation_point] = 1 - child[mutation_point]
    return child

def fitness_function(individual):
    return sum(individual)

if __name__ == "__main__":
    initial_population = [[random.randint(0, 1) for _ in range(10)] for _ in range(100)]
    best_individual = genetic_algorithm(initial_population, fitness_function, target_fitness=10)
    print("Best individual:", best_individual)
