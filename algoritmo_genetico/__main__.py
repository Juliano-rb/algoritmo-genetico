import crossover as crossover
import population as pop_utils

def get_population_stats(population, fitness_list):
    population_size = len(population)
    best_score = max(fitness_list, key=lambda fitness: fitness[1])
    best_element = population[best_score[0]]

    return population_size, best_score, best_element

def print_stats(population, fitness_list, generation_number):
    print()
    print("# generation " + str(generation_number) + " stats:", flush=True)
    # print("population:")
    # print(population)
    print(get_population_stats(population, fitness_list), flush=True)

def next_generation(population, next_generation_size, mutation_rate, mutation_impact, actual_generation):
    population = crossover.crossover_population(population, mutation_rate, mutation_impact)
    fitness_list = pop_utils.evaluate_population(population, print_progress=True)
    print_stats(population, fitness_list, actual_generation)
    population = pop_utils.selection(population, fitness_list, next_generation_size)

    return population

if __name__ == "__main__":
    init_population_size = 100
    mutation_rate = 0.4
    mutation_impact = 60 # something between 0 and this

    print("init_population_size = " + str(init_population_size))

    population = pop_utils.generate_population(init_population_size)
    print("population generated")

    generation_count = 0
    while (generation_count < 10):
        population = next_generation(population,
            init_population_size, 
            mutation_rate,
            mutation_impact,
            generation_count)
        generation_count+=1