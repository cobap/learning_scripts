#%%
from cyberbrain import trace

import numpy as np

#%%

# mutation operator


def mutation(bitstring, r_mut):
	for i in range(len(bitstring)):
		# check for a mutation
		if np.random.rand() < r_mut:
			# flip the bit
			bitstring[i] = 1 - bitstring[i]

# crossover two parents to create two children


def crossover(p1, p2, r_cross):
	# children are copies of parents by default
	c1, c2 = p1.copy(), p2.copy()
	# check for recombination
	if np.random.rand() < r_cross:
		# select crossover point that is not on the end of the string
		pt = np.random.randint(1, len(p1)-2)
		# perform crossover
		c1 = p1[:pt] + p2[pt:]
		c2 = p2[:pt] + p1[pt:]
	return [c1, c2]

# tournament selection


def selection(pop, scores, k=3):
	# first random selection
	selection_ix = np.random.randint(len(pop))
	for ix in np.random.randint(0, len(pop), k-1):
		# check if better (e.g. perform a tournament)
		if scores[ix] < scores[selection_ix]:
			selection_ix = ix
	return pop[selection_ix]


@trace
def genetic_algorithm(objective, n_bits, n_iter, n_pop, r_cross, r_mut):
    """
    Função básica de algoritmo genético

    Args:
        objective: função que queremos maximizar
        n_bits: representação genética do individuo
        n_iter: quantas interações desejamos fazer
        n_pop: tamanho da população desejada
        r_cross: taxa de crossover. 0 ~ 1
        r_mut: taxa de mutação. 0 ~ 1
    
    Returns:
        best: composição genética do indiviuo melhor avaliado
        best_eval: valor score da melhor avaliação

    """

    # initial population of random bitstring
    pop = [np.random.randint(0, 2, n_bits).tolist() for _ in range(n_pop)]
    # keep track of best solution
    best, best_eval = 0, objective(pop[0])
    # enumerate generations
    for gen in range(n_iter):
        # evaluate all candidates in the population
        scores = [objective(c) for c in pop]
        # check for new best solution
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
                print(">%d, new best f(%s) = %.3f" % (gen,  pop[i], scores[i]))
        # select parents
        selected = [selection(pop, scores) for _ in range(n_pop)]
        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i+1]
            # crossover and mutation
            for c in crossover(p1, p2, r_cross):
                # mutation
                mutation(c, r_mut)
                # store for next generation
                children.append(c)
        # replace population
        pop = children
    return [best, best_eval]

#%%

# Caso de uso: Problema OneMax


# 1) Criamos a função objetivo
def onemax(x): return -sum(x)


# 2) Definimos os hiperparametros
# define the total iterations
n_iter = 100
# bits
n_bits = 20
# define the population size
n_pop = 100
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 1.0 / float(n_bits)

# 3) Rodamos o algoritmo
best, score = genetic_algorithm(onemax, n_bits, n_iter, n_pop, r_cross, r_mut)
print('Done!')
print('f(%s) = %f' % (best, score))

#%%

# Caso de uso: Função Continua
