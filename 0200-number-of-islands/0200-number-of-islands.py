class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count_island = 0

        def dfs(row,col):
            # up , down , left then right 
            direction = [(-1,0),(1,0),(0,-1),(0,1)]
            grid[row][col] = "0"
            for row_dir , col_dir in direction:
                new_row = row_dir + row
                new_col = col_dir + col
                if not (0<= new_row < rows and 0<= new_col< cols):
                    continue
                if grid[new_row][new_col] == "0":
                    continue
                grid[new_row][new_col] = "0"

                dfs(new_row,new_col)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count_island += 1
                    dfs(i,j)
        return count_island