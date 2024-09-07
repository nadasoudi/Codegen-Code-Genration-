def floyd_warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > 0:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

graph = [[0, 4, 0, 0, 0],
         [4, 0, 8, 0, 0],