def shortest_path(graph, start, end):
    # Write your code here
    path = {}
    visited = {}
    for node in graph:
        path[node] = []
        visited[node] = False
    path[start] = []
    visited[start] = True
    while len(path[start])!= 0:
        current = path[start].pop(0)
        for node in graph[current]:
            if not visited[node]: