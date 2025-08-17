
def numberOfIslands(grid):
    if not grid:
        return 0

    res = 0
    rows, cols = len(grid), len(grid[0])

    def dfs(i ,j):
        if i >= rows or i < 0 or j >= cols or j < 0 or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                res += 1
                dfs(i, j)
    return res
