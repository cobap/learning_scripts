# Importamos o tipo de algoritmo genético, que nesse caso é continuo
from geneal.genetic_algorithms import ContinuousGenAlgSolver

# importamos uma função fitness continua 
from geneal.applications.fitness_functions.continuous import fitness_functions_continuous


# Inicializamos o solver com o número de genes e a função continua que precisa ser maximizada
solver = ContinuousGenAlgSolver(
    n_genes=4,
    fitness_function=fitness_functions_continuous(3),
    pop_size=10,  # population size (number of individuals)
    max_gen=200,  # maximum number of generations
    mutation_rate=0.1,  # mutation rate to apply to the population
    selection_rate=0.6,  # percentage of the population to select for mating
    selection_strategy="roulette_wheel",  # strategy to use for selection.
    problem_type=float,  # Defines the possible values as float numbers
    # Defines the limits of all variables between -10 and 10.
    variables_limits=(-10, 10)
    # Alternatively one can pass an array of tuples defining the limits
    # for each variable: [(-10, 10), (0, 5), (0, 5), (-20, 20)]
)

solver.solve()
