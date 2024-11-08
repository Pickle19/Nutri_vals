import random
from random import randint
import pandas as pd

data = pd.read_csv('food.csv', index_col=0)

# Genetic Algorithm parameters
population_size = 100
mutation_rate = 0.1
num_generations = 15
limit = 75

def create_individual():
    return [random.choice([0,1]) for _ in range(len(data))]

def create_pop():
    return [create_individual() for _ in range(population_size)]

def calc_fitness(individual, interest: str, type_of_food: str, interest_amount: int):
    total_price = 0
    total_interest = 0
    min_amount = 0

    for i in range(len(individual)):
        if individual[i] == 1:
            total_interest += data.loc[i+1][interest]
            total_price += data.loc[i+1]['Price']

            if data.loc[i+1]['Type'] == type_of_food:
                min_amount += 1

        if total_price > limit or min_amount < interest_amount:
            total_interest = 0

    return total_interest

#tournament selection
def parent_selection(population, interest, type_of_food, interest_amount):
    fitness_vals = [calc_fitness(individual, interest, type_of_food, interest_amount) for individual in population]
    random_individuals = random.sample(range(1,len(population)), 10)

    chosen = [(fitness_vals[i],population[i]) for i in random_individuals]
    chosen_sorted = sorted(chosen, key = lambda x:x[0], reverse=True)

    parent1, parent2 = chosen_sorted[0][1], chosen_sorted[1][1]
    return parent1, parent2

def crossover(parent1,parent2):
    crossover_point = randint(1,len(parent1)-1)

    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2

def mutation(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]


def geneticalgorithm(interest:str, type_of_food: str, interest_amount: int):
    population = create_pop()

    for _ in range(num_generations):
        new_population = []

        for _ in range(population_size // 2):
            parent1, parent2 = parent_selection(population, interest, type_of_food, interest_amount)
            child1, child2 = crossover(parent1, parent2)
            mutation(child1)
            mutation(child2)

            new_population.extend([child1,child2])

        population = new_population

        best_individual = max(population, key=lambda individual: calc_fitness(individual, interest, type_of_food, interest_amount))
        best_fit = calc_fitness(best_individual, interest, type_of_food, interest_amount)

    return best_individual, best_fit


best_solution, best_fitness = geneticalgorithm('Protein', 'meat', 2)

food_results = []
money_spent = 0
total_weight = 0

for i in range(len(best_solution)):
    if best_solution[i] == 1:
        food_results.append(data.loc[i+1]['Name'])
        money_spent += data.loc[i+1]['Price']
        total_weight += data.loc[i+1]['Item_weight']


print("Best Solution:", best_solution)
print("Food results:", food_results)
print('Money required (RON):', money_spent)
print("Best interest value (fitness):", best_fitness,"Out of:",len(food_results)*100,"grams")
# Itt még lehet gond