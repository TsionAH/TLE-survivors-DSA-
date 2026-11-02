from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        islands = 0

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        for row in range(rows):
            for col in range(cols):

                # Found a new island
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1

                    # Start BFS
                    queue = deque([(row, col)])
                    visited.add((row, col))

                    while queue:
                        current_row, current_col = queue.popleft()

                        for dr, dc in directions:
                            new_row = current_row + dr
                            new_col = current_col + dc

                            # Check grid boundaries
                            if not (0 <= new_row < rows and 0 <= new_col < cols):
                                continue

                            # Skip water or visited cells
                            if grid[new_row][new_col] == "0" or (new_row, new_col) in visited:
                                continue

                            # Mark visited and add to queue
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))

        return islands
      