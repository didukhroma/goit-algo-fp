


# def plot_probabilities(probabilities,titles):
#     fig, axes = plt.subplots(2, 2, figsize=(12, 8))
#     axes = axes.flatten()

#     for i, (probabilities, ax) in enumerate(zip(prob_list, axes)):
#         sorted_data = sorted(probabilities.items(), key=lambda x: x[0])
#         x = [key for key, _ in sorted_data]
#         y = [value for _, value in sorted_data]

#         ax.bar(x, y)
#         ax.set_xlabel("Сума")
#         ax.set_ylabel("Ймовірність, %")
#         if titles:
#             ax.set_title(titles[i])
#         else:
#             ax.set_title(f"Графік {i+1}")

#     plt.tight_layout()
#     plt.show()

