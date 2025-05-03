import random
from collections import defaultdict
from tabulate import tabulate
import matplotlib.pyplot as plt

def monte_carlo_simulating(number_of_simulations):
    result= defaultdict(int)
    for _ in range(number_of_simulations):
        total = random.randint(1,6) + random.randint(1,6)
        result[total] += 1
    for key in result:
        result[key] /= number_of_simulations / 100
    return result

def display_probabilities(probabilities,simulations):
    table = []
    table_header = ["Sum", *[f"{value} simulations" for value in simulations]]   
    for key in probabilities.keys():        
        data= [key, *[f"{value:.2f} %" for value in probabilities[key]]]
        table.append(data)
    print(tabulate(table, headers=table_header))


simulations = [100, 1000, 10000, 100000]
probabilities = {2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[], 11:[], 12:[]}
for i in simulations:
    data = monte_carlo_simulating(i)
    for key in probabilities.keys():
        probabilities[key].append(data[key])

display_probabilities(probabilities,simulations)



