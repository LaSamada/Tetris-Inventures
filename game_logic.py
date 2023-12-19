from grid import Grid
from blocks import *
import random, pygame


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.game_over = False
        self.level = 1
        self.lines_completed = 0
        self.time = int(1000 * (0.8 - ((self.level - 1) * 0.007)) ** (self.level - 1))

    def next_level(self):
        self.level += 1
        self.time = int(1000 * (0.8 - ((self.level - 1) * 0.007)) ** (self.level - 1))
        self.lines_completed = 0

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block
    
    def update_score(self, lines_clear, move_down_points, hard_drop_rows): #falta nivel y varios
        if lines_clear == 1:
            self.score += 100 * self.level
        elif lines_clear == 2:
            self.score += 300 * self.level
        elif lines_clear == 3:
            self.score += 500 * self.level
        elif lines_clear == 4:
            self.score += 800 * self.level
        self.score += move_down_points
        self.score += 2 * hard_drop_rows


    def paint(self, surface):
        self.grid.paint(surface)
        self.current_block.paint(surface, 301, 1)
        self.next_block.paint(surface, 20, 250)

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), ZBlock(), TBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.level = 1

    def move_left(self):
        self.current_block.movement(0, -1)
        if self.block_inside() == False or self.collision() == True:
            self.current_block.movement(0, 1)

    def move_right(self):
        self.current_block.movement(0, 1)
        if self.block_inside() == False or self.collision() == True:
            self.current_block.movement(0, -1)

    def soft_drop(self):
        self.current_block.movement(1, 0)
        if self.block_inside() == False or self.collision() == True:
            self.current_block.movement(-1, 0)
            self.lock_block()

    def hard_drop(self):
        n_rows_drop = 0
        while self.collision() == False:
            n_rows_drop += 1
            self.current_block.movement(1, 0)
            if self.block_inside() == False or self.collision() == True:
                self.current_block.movement(-1, 0)
                n_rows_drop -= 1
                self.lock_block()
                return n_rows_drop

    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False  or self.collision() == True:
            self.current_block.undo_rotate()

    def lock_block(self):
        tiles = self.current_block.paint_movement()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.shape
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.lines_completed += rows_cleared
        self.update_score(rows_cleared, 0, 0)
        if self.lines_completed >= 10:
            self.next_level()
        if self.collision() == True:
            self.game_over = True

    def block_inside(self):
        tiles = self.current_block.paint_movement()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def collision(self):
        tiles = self.current_block.paint_movement()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return True
        return False