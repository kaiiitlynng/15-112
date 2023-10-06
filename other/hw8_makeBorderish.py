#################################################
# hw8.py
# name: Kaitlyn Ng
# andrew id: kgn
#################################################

from cmu_graphics import *
import math, copy

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Complete makeBorderish(L) below
#################################################

def makeBorderish(L):
    rows, cols = len(L), len(L[0])
    for colA in range(cols):
        for colB in range(cols):
            if colA != colB:
                swapCols(L, colA, colB)
                if not isBorderish(L):
                    swapCols(L, colB, colA)
                else:
                    return #None to prevent more swaps

def swapCols(L, col0, col1):
    rows, cols = len(L), len(L[0])
    for row in range(rows):
        L[row][col0], L[row][col1] = L[row][col1], L[row][col0]

def isBorderish(L):
    rows, cols = len(L), len(L[0])
    sumBord = 0
    sumInt = 0
    maxRow = max([i for i in range(rows)])
    maxCol = max([i for i in range(cols)])

    for row in range(rows):
        for col in range(cols):
            if row == 0 or row == maxRow:
                sumBord += L[row][col]
            elif col == 0 or col == maxCol:
                sumBord += L[row][col]
            else:
                sumInt += L[row][col]
    return sumBord == sumInt

#################################################
# (Don't modify anything below here)
#################################################
# Test Functions
#################################################

def testMakeBorderish():
    print('Testing makeBorderish()...', end='')
    L = [ [ 1, 0, 2, 1 ],
          [ 2, 5, 0, 4 ],
          [ 1, 1, 1, 0 ]
        ]
    M = [ [ 1, 0, 1, 2 ],
          [ 2, 5, 4, 0 ],
          [ 1, 1, 0, 1 ]
        ]
    assert(makeBorderish(L) == None)
    assert(L == M)

    L = [ [ 2, 0, 1 ],
          [ 8, 0, 2 ],
          [ 1, 1, 1 ]
        ]
    M = [ [ 0, 2, 1 ],
          [ 0, 8, 2 ],
          [ 1, 1, 1 ]
        ]
    assert(makeBorderish(L) == None)
    assert(L == M)

    L = [ [ 2, 0, 1 ],
          [ 8, 0, 2 ],
          [ 5, 1, 1 ],
          [ 1, 2, 3 ]
        ]
    M = [ [ 0, 2, 1 ],
          [ 0, 8, 2 ],
          [ 1, 5, 1 ],
          [ 2, 1, 3 ]
        ]
    assert(makeBorderish(L) == None)
    assert(L == M)
    print('Passed')

#################################################
# Test animation 
#################################################

def onAppStart(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.dx = 2
    app.dy = 1
    app.rectWidth = 100
    app.rectHeight = 50
    
def onMousePress(app, mouseX, mouseY):
    app.cx = mouseX
    app.cy = mouseY

def onStep(app):
    left = app.cx - app.rectWidth/2
    right = app.cx + app.rectWidth/2
    top = app.cy - app.rectHeight/2
    bottom = app.cy + app.rectHeight/2
    if left < 0: app.dx = abs(app.dx)
    elif right > app.width: app.dx = -abs(app.dx)

    if top < 0: app.dy = abs(app.dy)
    elif bottom > app.height: app.dy = -abs(app.dy)

    app.cx += app.dx
    app.cy += app.dy

def redrawAll(app):
    drawRect(app.cx, app.cy, app.rectWidth, app.rectHeight, 
             align = 'center', fill = 'green')
    drawLabel("Nice", app.cx, app.cy, size = 20, fill = 'white')
    drawLabel("cmu_graphics is installed!", app.width/2, 20, size = 20)
    
#################################################
# main
#################################################

def main():
    testMakeBorderish()
    runApp()

if __name__ == '__main__':
    main()
