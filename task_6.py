items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    sorted_items = sorted(items.items(), key = lambda item: item[1]["calories"] / item[1]["cost"])
    total_calories = 0
    selected_dishes = []
    for item in sorted_items:
        if budget >= item[1]["cost"]:
            budget -= item[1]["cost"]
            total_calories += item[1]["calories"]
            selected_dishes.append(item[0])
    return selected_dishes, total_calories     

def dynamic_programming(budget):
    n = len(items)
    wt = [items[dish]["calories"] for dish in items]
    val = [items[dish]["cost"] for dish in items]
    W = budget
    K = [[0 for w in range(W + 1)] for i in range(n + 1)]

    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    total_calories = K[n][W]
    selected_dishes = []
    i = n
    while i > 0 and W > 0:
        if K[i][W] == K[i - 1][W]:
            i -= 1
        else:
            selected_dishes.append(list(items.keys())[i - 1])
            W -= wt[i - 1]
            i -= 1
    return selected_dishes, total_calories

budget = int(input("Enter your budget: "))
selected_dishes, total_calories = greedy_algorithm(budget)
print("Greedy algorithm:")
print("Selected dishes:", selected_dishes)
print("Total calories:", total_calories)

print("\nDynamic programming:")
selected_dishes, total_calories = dynamic_programming(budget)
print("Selected dishes:", selected_dishes)
print("Total calories:", total_calories)