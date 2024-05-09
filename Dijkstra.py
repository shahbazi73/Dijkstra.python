def min_distance(distances, visited):
    min_val = float('inf')
    min_index = -1

    for i in range(len(distances)):
        if distances[i] < min_val and i not in visited:
            min_val = distances[i]
            min_index = i

    return min_index


def dijkstra_algorithm(graph, start_node):

    num_nodes = len(graph)

    distances = [float('inf')] * num_nodes
    # print(distances)
    # # exit()
    visited = []

    distances[start_node] = 0

    for i in range(num_nodes):

        current_node = min_distance(distances, visited)

        visited.append(current_node)

        for j in range(num_nodes):

            if graph[current_node][j] != 0:

                new_distance = distances[current_node] + graph[current_node][j]

                if new_distance < distances[j]:
                    distances[j] = new_distance

    return distances

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]

shortest_distances = dijkstra_algorithm(graph, 0)

print(shortest_distances)