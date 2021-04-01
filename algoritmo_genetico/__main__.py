import crossover as crossover
import population as pop_utils

if __name__ == "__main__":
    init_population_size = 5
    next_generation_size = round(init_population_size*0.3)

    print("init_population_size = " + str(init_population_size))
    print("next_generation_size = " + str(next_generation_size))

    population = pop_utils.generate_population(init_population_size)

    new_population = crossover.crossover_population(population)

    fitness_list = pop_utils.evaluate_population(new_population)

    selected_population = pop_utils.selection(population, fitness_list, next_generation_size)
