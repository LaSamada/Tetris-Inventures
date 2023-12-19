from miscellaneous import Position
from block import Block

class IBlock(Block):
    def __init__(self):
        super().__init__(shape = 1)
        self. cells = {
            0 : [Position(1,0), Position(1,1), Position(1,2), Position(1,3)],
            1 : [Position(0,2), Position(1,2), Position(2,2), Position(3,2)],
            2 : [Position(2,0), Position(2,1), Position(2,2), Position(2,3)],
            3 : [Position(0,1), Position(1,1), Position(2,1), Position(3,1)]
        }
        self.movement(-1,3)

class JBlock(Block):
    def __init__(self):
        super().__init__(shape = 2)
        self. cells = {
            0 : [Position(0,0), Position(1,0), Position(1,1), Position(1,2)],
            1 : [Position(0,1), Position(1,1), Position(2,1), Position(0,2)],
            2 : [Position(1,0), Position(1,1), Position(1,2), Position(2,2)],
            3 : [Position(0,1), Position(1,1), Position(2,1), Position(2,0)]
        }
        self.movement(0,3)

class LBlock(Block):
    def __init__(self):
        super().__init__(shape = 3)
        self. cells = {
            0 : [Position(0,2), Position(1,0), Position(1,1), Position(1,2)],
            1 : [Position(0,1), Position(1,1), Position(2,1), Position(2,2)],
            2 : [Position(1,0), Position(1,1), Position(1,2), Position(2,0)],
            3 : [Position(0,1), Position(1,1), Position(2,1), Position(0,0)]
        }
        self.movement(0,3)

class OBlock(Block):
    def __init__(self):
        super().__init__(shape = 4)
        self. cells = {
            0 : [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            1 : [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            2 : [Position(0,0), Position(0,1), Position(1,0), Position(1,1)],
            3 : [Position(0,0), Position(0,1), Position(1,0), Position(1,1)]
        }
        self.movement(0,4)

class SBlock(Block):
    def __init__(self):
        super().__init__(shape = 5)
        self. cells = {
            0 : [Position(1,0), Position(1,1), Position(0,1), Position(0,2)],
            1 : [Position(0,1), Position(1,1), Position(1,2), Position(2,2)],
            2 : [Position(1,2), Position(1,1), Position(2,1), Position(2,0)],
            3 : [Position(0,0), Position(1,1), Position(1,0), Position(2,1)]
        }
        self.movement(0,3)

class ZBlock(Block):
    def __init__(self):
        super().__init__(shape = 6)
        self. cells = {
            0 : [Position(0,0), Position(1,1), Position(0,1), Position(1,2)],
            1 : [Position(0,2), Position(1,1), Position(1,2), Position(2,1)],
            2 : [Position(1,0), Position(1,1), Position(2,1), Position(2,2)],
            3 : [Position(0,1), Position(1,0), Position(1,1), Position(2,0)]
        }
        self.movement(0,3)

class TBlock(Block):
    def __init__(self):
        super().__init__(shape = 7)
        self. cells = {
            0 : [Position(0,1), Position(1,0), Position(1,1), Position(1,2)],
            1 : [Position(1,2), Position(0,1), Position(1,1), Position(2,1)],
            2 : [Position(2,1), Position(1,0), Position(1,1), Position(1,2)],
            3 : [Position(1,0), Position(0,1), Position(1,1), Position(2,1)]
        }
        self.movement(0,3)