# %%

# Agent Bee Colony

# Podemos rodar esse algoritmo em paralelo, o que nos dá larga vantagem computacional!

# https://towardsdatascience.com/implementing-artificial-bee-colony-algorithm-to-solve-business-problems-cb754f3b9255
# https://towardsdatascience.com/how-to-apply-artificial-bee-colony-algorithm-to-solve-unconventional-problems-a41c5098eb3a

# How it works?

# Food source = Problem Solutions
# Employed bees = Agents - Go from food source to food source (Random, but always keep next to food sources)
# Onlooker bees = Agents - Learn from employed bees Roulette Wheel Selection Algorithm
# Scout bees = Choose their food sources randomly to replace abandoned food sources that cannot be improved any further after # trails

# %%

# We generate initial location for each bee in the space
def initializeFoodSources():
    pass

# 
def sendEmployedBees(food_sources):
    
    # Each bee go to the food source they remember
    for food_source in food_sources:
        pass

    # Evaluate nectar amount (loss function)
    if new_nectar_amount > old_nectar_amount:
        # Update food source
        pass
    else:
        # Update trails
        pass

def sendOnlookerBees():

    # There are many onlookers as food sources

    # For each onlooker. Roulette Wheel Selection Algorithm
    # Based on probability, check food source and change it. Same as employed
    # REVIEW: Difference

def sendScoutBees():

    # When a location was tested so much, it's abandoned
    pass

bestFoodSource = None
maxCicles = 1000

# Initialize random food sources on the environment
initializeFoodSources()

for i in range(maxCicles):

    # Send employed bees to each food source. They return with nectar
    # Update the food sources
    sendEmployedBees()
    updateProbabilities()

    # Now onlooker will explore the food souces region, replacing with better food sources when found
    sendOnlookerBees()
    # Memorize the best locations
    memorizeBestFoodSource()

    # Replace food source with high trial from food source found by scout
    sendScoutBees()
