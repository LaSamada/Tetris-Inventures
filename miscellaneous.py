import pygame

class Colors:
        black = (0,0,0)
        light_blue = (110, 255, 255)
        dark_blue = (0,0,139)
        orange = (255, 165, 0)
        yellow = (255,255,0)
        green = (127,255,0)
        red = 	(255,0,0)
        magenta = (255,0,255)
        white = (255, 255, 255)
        gray = (58, 58, 58)

        @classmethod
        def cell_colors(cls):
            return [cls.black, cls.light_blue, cls.dark_blue, cls.orange, cls.yellow, cls.green,
            cls.red, cls.magenta]

class Position:
    def __init__(self, row, column):
        self.row = row
        self.column = column