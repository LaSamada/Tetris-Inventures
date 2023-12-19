import pygame
from miscellaneous import Position, Colors

class Block:
    def __init__(self, shape):
        self.shape = shape
        self.cells = {}
        self.cell_size = 30
        self.rotation = 0
        self.colors = Colors.cell_colors()
        self.column_offset = 0
        self.row_offset = 0

    def movement(self, rows, columns):
        self.column_offset += columns
        self.row_offset += rows


    def paint_movement(self):
        tiles = self.cells[self.rotation]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column +
            self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    def rotate(self):
        self.rotation += 1
        if self.rotation > 3:
            self.rotation = 0

    def undo_rotate(self):
        self.rotation -= 1
        if self.rotation < 0:
            self.rotation = 3

    def paint(self, surface, offset_x, offset_y):
        tiles = self.paint_movement()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, offset_y + tile.row *
            self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(surface, self.colors[self.shape], tile_rect)