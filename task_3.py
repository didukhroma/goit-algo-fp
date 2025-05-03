import heapq

test_graph = {
    "Market Square": {
        "Castle Street": 3,
        "Bus Station": 5,
        "Kisvarda Castle": 7
    },
    "Castle Street": {
        "City Hospital": 2,
        "Market Square": 3,
        "Rakoczi Street": 4  
    },
    "City Hospital": {
        "Bus Station": 4,
        "Vasarosnameny Road": 6  
    },
    "Bus Station": {
        "Rakoczi Street": 3,
        "Market Square": 5,
        "City Hospital": 4
    },
    "Rakoczi Street": {
        "Vasarosnameny Road": 5,
        "Castle Street": 4,
        "Bus Station": 3  
    },
    "Vasarosnameny Road": {
        "Kisvarda Castle": 6,
        "City Hospital": 6  
    },
    "Kisvarda Castle": {
        "Market Square": 7,
        "Vasarosnameny Road": 6  
    }
}

def dijkstra (graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if distances[current_vertex] == float('inf'):
            break

        for neighbor,weight in graph[current_vertex].items():
            distance  = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, [distance, neighbor])
      
    return distances
    

print(dijkstra(test_graph, "Bus Station"))