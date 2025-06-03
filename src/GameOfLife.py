import numpy as np

class GameOfLife:

    def __init__(self, width, height, density):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int)
        self.init_grid(density)

    def count_neighbors(self, x, y, grid):
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                if x + dx < 0 or x + dx >= self.width:
                    continue
                if y + dy < 0 or y + dy >= self.height:
                    continue
                nx = x + dx
                ny = y + dy
                count += grid[ny][nx]
                # print(count)
        return count


    def change_cell(self, x, y, grid):
        neighbors = self.count_neighbors(x, y, grid)
        if grid[y][x] == 0 and neighbors == 3:
            self.grid[y][x] = 1
        elif grid[y][x] == 1 and neighbors in [2, 3]:
            self.grid[y][x] = 1
        else:
            self.grid[y][x] = 0


    def update(self):
        current_state = np.copy(self.grid)

        for y in range(self.height):
            for x in range(self.width):
                self.change_cell(x, y, current_state)

    def init_grid(self, density):
        for y in range(self.height):
            for x in range(self.width):
                num = np.random.randint(0, density)
                if num == 0:
                    self.grid[y][x] = 1

    def clear(self):
        self.grid = np.zeros((self.height, self.width), dtype=int)

