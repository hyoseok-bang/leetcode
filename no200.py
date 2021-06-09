# https://leetcode.com/problems/number-of-islands/

def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    def dfs(i,j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = 0  # mark as "visited"

        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i,j+1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i,j)  # search terminates if all the visited areas are water
                count += 1

    return count
