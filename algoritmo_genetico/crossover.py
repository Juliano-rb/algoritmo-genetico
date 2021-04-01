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