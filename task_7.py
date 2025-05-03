'''
Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.



Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.



На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
'''

import random
from collections import defaultdict
import matplotlib.pyplot as plt

def monte_carlo_simulating(number_of_simulations):
    result= defaultdict(int)
    for _ in range(number_of_simulations):
        total = random.randint(1,6) + random.randint(1,6)
        result[total] += 1
    for key in result:
        result[key] /= number_of_simulations / 100
    return result

def display_probabilities(probabilities):
    sorted_data = sorted(probabilities.items(), key=lambda x: x[0])
    print("+-------+-------------+")
    print("| Сума  | Ймовірність |")
    print("+-------+-------------+")
    for key, value in sorted_data:
         print(f"| {key:<5} | {f"{value:.2f}%":11} |")
    print("+-------+-------------+")

def plot_probabilities(probabilities):
    sorted_data = sorted(probabilities.items(), key=lambda x: x[0])
    x = [key for key, _ in sorted_data]
    y = [value for _, value in sorted_data]
    plt.bar(x, y)
    plt.xlabel("Сума")
    plt.ylabel("Імовірність,%")
    plt.title("Імовірність кожної суми")
    plt.show()

data = monte_carlo_simulating(10000)
display_probabilities(data)
plot_probabilities(data)

