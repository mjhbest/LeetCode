class Solution:    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            
        maxIsland = 0
        w, h = len(grid), len(grid[0])
        
        for i in range(w):
            for j in range(h):
                if grid[i][j] == 1 :
                    newIsland = self.expendIsland(grid,i,j,w,h)
                    maxIsland = max(maxIsland, newIsland)
        
        return maxIsland
    
    def expendIsland(self, grid, x, y, w, h):
        if x < 0 or y<0 or x>=w or y>=h:
            return 0
        
        if grid[x][y] == 0:
            return 0
        
        print(x,y)
        count = 1
        grid[x][y] = 0
        
        count += self.expendIsland(grid, x-1, y, w, h)
        count += self.expendIsland(grid, x+1, y, w, h)
        count += self.expendIsland(grid, x, y-1, w, h)
        count += self.expendIsland(grid, x, y+1, w, h)
        
        return count
        
        
        