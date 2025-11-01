from copy import deepcopy
from collections import deque
class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        queue = deque()
        image_copy = deepcopy(image)
        initial = image_copy[sr][sc]
        if image_copy[sr][sc] == color:
            return image_copy
            
        image_copy[sr][sc] = color
        queue.append((sr, sc))

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                i, j = x + dx, y + dy
                if i < 0 or i >= len(image_copy) or j < 0 or j >= len(image_copy[0]):
                    continue
                if image_copy[i][j] != initial:
                    continue

                image_copy[i][j] = color
                queue.append((i, j))
        return image_copy