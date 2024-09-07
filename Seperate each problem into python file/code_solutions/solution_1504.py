grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

"""

grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end=" ")
        print()