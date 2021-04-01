import random

def try_mutation(individual, mutation_rate, mutation_amount=20):
    # print(mutation_rate, mutation_amount)
    gene_length = len(individual)
    n = random.random()
    mutation_impact = round(random.uniform(-mutation_amount, mutation_amount))

    new_individual = individual.copy()
    if (mutation_rate > n):
        mutation_target = random.randint(0,gene_length-1)
        new_individual[mutation_target]+=mutation_impact
        # impedir que o individuo fique inconsistente
        if(new_individual[mutation_target] < 0):
            new_individual[mutation_target] = 0
        if(new_individual[mutation_target] > 360):
            new_individual[mutation_target] = 360
        # print(individual, new_individual)
        return new_individual
    
    return individual

def crossover(individual1, individual2, mutation_rate, mutation_impact):
    gene_length = len(individual1)
    division_pos = random.randint(1,gene_length-1)
    # division_pos = round(gene_length/2)
    
    new_gene_start = individual1[:division_pos]
    new_gene_end = individual2[division_pos:]

    new_individual = new_gene_start + new_gene_end
    new_individual = try_mutation(new_individual, mutation_rate, mutation_impact)
    return new_individual

def crossover_population(population, mutation_rate = 0.1, mutation_impact=20):
    # print("crossing population")
    # print(population)
    new_population = []

    # crossover everyone with everyone
    for individual1 in population:
        for individual2 in population:
            if(individual1 != individual2):
                children = crossover(individual1, individual2, mutation_rate, mutation_impact)
                new_population.append(children)
    
    population.extend(new_population)

    return population