import fitness
import random
population = []

def get_random_gene():
    amplitude = 360
    gene = random.randint(0, amplitude)

    return gene

def generate_population(size):
    chromosome_size = 6

    population = []
    for i in range(size):
        chromosome = []
        for g in range(chromosome_size):
            gene = get_random_gene()
            chromosome.append(gene)
        population.append(chromosome)
    return population

def evaluate_population(population):
    fitness_list =[]
    index = 0
    for individual in population:
        score = fitness.get_fitness(individual)
        fitness_list.append((index,score))

        index += 1
    
    return fitness_list

def selection(population, fitness_list, new_generation_size ):
    # ordena a lista de fitness pelo score
    fitness_list = sorted(fitness_list, key=lambda fitness: fitness[1])

    new_population = []
    for f in fitness_list:
        if (len(new_population) >= new_generation_size):
            break

        index = f[0]
        new_population.append(population[index])
    
    return new_population

def crossover(individual1, individual2):
    # print("crossover: ")
    # print(individual1)
    # print(individual2)

    gene_length = len(individual1)
    
    new_gene_start = individual1[:round(gene_length/2)]
    new_gene_end = individual2[round(gene_length/2):]

    new_individual = new_gene_start + new_gene_end

    # print("result: ")
    # print(new_individual)

    return new_individual

def crossover_population(population):
    # print("crossing population")
    # print(population)
    new_population = []

    # crossover everyone with everyone
    for individual1 in population:
        for individual2 in population:
            if(individual1 != individual2):
                children = crossover(individual1, individual2)
                new_population.append(children)
    
    population.extend(new_population)

    return population


if __name__ == "__main__":
    init_population_size = 5
    next_generation_size = round(init_population_size*0.3)

    print("init_population_size = " + str(init_population_size))
    print("next_generation_size = " + str(next_generation_size))

    population = generate_population(init_population_size)

    new_population = crossover_population(population)

    fitness_list = evaluate_population(new_population)

    selected_population = selection(population, fitness_list, next_generation_size)

    # print(selected_population)
