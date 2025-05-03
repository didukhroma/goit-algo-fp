items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(budget):
    sorted_items = sorted(items.items(), key = lambda item: item[1]["calories"] / item[1]["cost"], reverse=True)
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
    item_names = list(items.keys())
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    trace = [[False for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        name = item_names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        for j in range(budget + 1):
            dp[i][j] = dp[i - 1][j]
            if cost <= j:
                if dp[i - 1][j - cost] + calories > dp[i][j]:
                    dp[i][j] = dp[i - 1][j - cost] + calories
                    trace[i][j] = True

    selected_items = []
    current_budget = budget
    for i in range(n, 0, -1):
        if trace[i][current_budget]:
            name = item_names[i - 1]
            selected_items.append(name)
            current_budget -= items[name]["cost"]

    return  selected_items,dp[n][budget]

budget = int(input("Enter your budget: "))
selected_dishes, total_calories = greedy_algorithm(budget)
print("Greedy algorithm:")
print("Selected dishes:", selected_dishes)
print("Total calories:", total_calories)

print("\nDynamic programming:")
selected_dishes, total_calories = dynamic_programming(budget)
print("Selected dishes:", selected_dishes)
print("Total calories:", total_calories)