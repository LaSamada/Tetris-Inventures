import numpy as np, pygame
from miscellaneous import Colors
class Grid:
    def __init__(self):
        self.cols = 10
        self.rows = 20
        self.grid = np.zeros((self.rows, self.cols), int)
        self.cell_size = 30
        self.colors = Colors.cell_colors()

    def reset(self):
        self.grid = np.zeros((self.rows, self.cols), int)

    def is_inside(self, row, column):
        if row >= 0 and row < self.rows and column >= 0 and column < self.cols:
            return True
        return False
    
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False
    
    def is_row_full(self, row):
        for column in range(self.cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def clear_row(self, row):
        self.grid[row][:] = 0
    
    def move_row_down(self, row, n_rows):
        self.grid[row + n_rows][:] = self.grid[row][:]
        self.grid[row][:] = 0

    def clear_full_rows(self):
        completed = 0
        for row in range(self.rows - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def paint(self, surface):
        for row in range(self.rows):
            for column in range(self.cols):
                cell_value = self.grid[row][column]
                cell_rect = pygame.Rect(column * self.cell_size + 301, row * self.cell_size + 1,
                self.cell_size - 1, self.cell_size - 1)
                pygame.draw.rect(surface, self.colors[cell_value], cell_rect)