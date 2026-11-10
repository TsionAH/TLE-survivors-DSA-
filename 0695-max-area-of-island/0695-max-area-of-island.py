class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        
        max_return = 0
        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(roww,colum):
            if grid[roww][colum] == 0:
                return 0
            
            grid[roww][colum] = 0
            direction = [(-1,0),(1,0),(0,-1),(0,1)]
            count = 1
            for row, col in direction:
                new_row = roww + row
                new_col = colum + col
                if not (0<= new_row < rows and 0<=new_col < cols):
                    continue
                
                count += dfs(new_row,new_col)
            return count
        for parts in range(rows):
            for j in range(cols):
                if grid[parts][j] == 1:
                    
                    max_return = max(max_return,dfs(parts,j))
        return max_return