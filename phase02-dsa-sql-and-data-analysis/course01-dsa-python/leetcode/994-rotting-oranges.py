from copy import deepcopy
from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:
        queue = deque()
        grid_copy = deepcopy(grid)
        fresh_oranges = 0
        minutes = 0

        for r in range(len(grid_copy)):
            for c in range(len(grid_copy[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        while queue and fresh_oranges > 0:
            minutes += 1
            level_size = len(queue)

            for rotten in range(level_size):
                i, j = queue.popleft()

                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_i, new_j = i + dx, j + dy

                    if new_i < 0 or new_i >= len(grid_copy) or new_j < 0 or new_j >= len(grid_copy[0]):
                        continue
                    if grid_copy[new_i][new_j] == 2 or grid_copy[new_i][new_j] == 0:
                        continue

                    grid_copy[new_i][new_j] = 2
                    fresh_oranges -= 1
                    queue.append((new_i, new_j))
                
        if fresh_oranges > 0:
            return -1
        return minutes