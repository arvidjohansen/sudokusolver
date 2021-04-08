
from array import *
from varinfo import *
from random import randint


class Pos():
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return f'{self.val}'




def colvals(board,col):
    ret = []
    for row in board:
        ret.append(row[col])
    return ret


def setup():
    rows = []
    counter = 0
    for y in range(1,10):
        row = []
        while len(row) != 9:
            val = randint(1,9)
            if val not in row and val:
                row.append(val)
        rows.append(row)
    return rows
b = setup()
print(b)
#board = [[Pos(randint(1,10)) for y in range(1,10)] for x in range(1,10)]

#class Board():
#    def find_
"""
class Board():
    rows = [] 

    def col(i):
        ret = []
        for r in self.rows:
            ret.append(r[i])
        return ret

"""

"""
def get_cols(board):
    pass

def setup():
    rows = []
    while len(rows) != 9:
        row = []
        while len(row) != 9:
            val = rn()
            if val not in row:
                row.append(val)
        rows.append(row)
    return rows
"""

"""
class Board():
    data = [
        [None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None],
    ]

    def get(self, x,y):
        return self.data[x][y]
    
    def set(self,x,y, val):
        self.data[x][y] = val
    
    def rows (self):
        return [r for in in self.data if r ]
"""
"""
def _pre_setup():
    board = [[None for s in range(9)] for r in range(9)]
    return board

b = _pre_setup()

def rn():
    return randint(1,9)
    

print(b)

def setup():
    

    global b

    def colvals(i):
        return [b[i] for r in b]
    
    for i in range(9):
        for j in range(9):
            val = rn()
            if val not in b[i]:
                b[i][j]
    
setup()
    
print(b)

#b = Board()

"""
"""

def rval(): 
    return randint(1,9)

def rpos(): 
    return randint(0,8)


def rand_setup():
    global b
    cont = True
    while cont:
        x = rpos()
        y = rpos()
        v = rval()

        b.set(x,y,v)
        
        if len(b.data) == 9:
            for row in b.data:
                if len(row) == 9:
                    cont = False
        
    return b



b = rand_setup()
print(b.data)
""" 

"""
def setup():
    rows = []
    for y in range(1,10):
        row = []
        while len(row) != 9:
            val = randint(1,9)
            if val not in row:
                row.append(val)
        rows.append(row)
    return rows
"""


"""
board = []
for y in range(1,10):
    for x in range(1,10):
        board.append(Pos(x,y))
"""

"""
def showboard():
    global board
    for r in board:
        print(r) 

print(showboard())
"""