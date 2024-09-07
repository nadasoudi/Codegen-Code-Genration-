def topologicalSort(arr):
    visited = [False] * len(arr)
    stack = []
    for i in range(len(arr)):
        if visited[i] == False:
            visited[i] = True
            stack.append(i)
            while len(stack) > 0:
                top = stack.pop()
                arr[top] = arr[top] + 1
                if top!= i:
                    visited[top] = False