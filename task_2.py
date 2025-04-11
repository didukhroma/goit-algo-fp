'''
Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії.
'''
from matplotlib import pyplot as plt
import math

def draw_pifagor_tree(level, x, y, length, angle):
    if level == 0:
        return
    
    x2 = x + length * math.cos(angle)
    y2 = y + length * math.sin(angle)
    plt.plot([x, x2], [y, y2], color='green')
    
    new_length = length * 0.7    
    draw_pifagor_tree(level - 1, x2, y2, new_length, angle + math.pi / 3)
    draw_pifagor_tree(level - 1, x2, y2, new_length, angle - math.pi / 3)

level = int(input("Enter the level of recursion: "))
plt.figure(figsize=(10, 10))
draw_pifagor_tree(level, 0, 0, 100, math.pi / 2)
plt.axis('off')
plt.title("Pifagor Tree")
plt.show()