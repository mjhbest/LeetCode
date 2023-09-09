class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    ans = max(ans, self.dfs(i, j, grid))
        return ans
    
    def dfs(self, i: int, j: int, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = grid[i][j]
        grid[i][j] = 0
        for a, b in pairwise((-1, 0, 1, 0, -1)):
            x, y = i + a, j + b
            if 0 <= x < m and 0 <= y < n and grid[x][y]:
                cnt += self.dfs(x, y, grid)
        return cnt
        