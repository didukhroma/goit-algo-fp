import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
      self.left = None
      self.right = None
      self.val = key
      self.color = color    # Додатковий аргумент для зберігання кольору вузла
      self.id = str(uuid.uuid4())   # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
      graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
      if node.left:
          graph.add_edge(node.id, node.left.id)
          l = x - 1 / 2 ** layer
          pos[node.left.id] = (l, y - 1)
          l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
      if node.right:
          graph.add_edge(node.id, node.right.id)
          r = x + 1 / 2 ** layer
          pos[node.right.id] = (r, y - 1)
          r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root,title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(9, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_tree_from_heap(arr):
    arr = [-item for item in arr]
    heapq.heapify(arr)
    
    nodes = [Node(-value) for value in arr]  

    for i in range(len(nodes) // 2):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]    
    return nodes[0]

def bfs(root):
    from collections import deque

    visited = set()
    queue = deque([root])
    color_step = 0x111111
    start_color = "#1296F0"
    current_color_int = int(start_color.lstrip('#'), 16)

    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)

        node.color = f"#{current_color_int:06X}"
        current_color_int = max(0, current_color_int + color_step)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return root


def dfs(root):
    stack = [root]
    color_step = 0x111111
    start_color = "#1296F0"
    current_color_int = int(start_color.lstrip('#'), 16)

    while stack:
        node = stack.pop()
        node.color = f"#{current_color_int:06X}"
        current_color_int = max(0, current_color_int + color_step)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return root

# Відображення дерев
test_arr = [1, 4, 3, 5, 10, 0, 2]

root = build_tree_from_heap(test_arr)
root_bfs = build_tree_from_heap(test_arr)
root_dfs = build_tree_from_heap(test_arr)

bfs_tree = bfs(root_bfs)
dfs_tree = dfs(root_dfs)

draw_tree(root,"Original tree")
draw_tree(bfs_tree,"BFS tree")
draw_tree(dfs_tree,"DFS tree")


