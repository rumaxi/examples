from board import Board
import pyscreenshot as ig
import cv2
import time
from stockfish import Stockfish

board   = Board()
e       = Stockfish()

'''
print (board.image(img))
print (fen)
m   = e.getmove(fen)['move']


sleep (1)

'''

while True:
    ig.grab_to_file('/tmp/ss.png')
    img = cv2.imread ('/tmp/ss.png')
    board.image(img)
    fen = board.fen()
    m = e.getmove(fen)['move']
    board.move(m)
    ig.grab_to_file('/tmp/ss.png')
    img = cv2.imread ('/tmp/ss.png')
    board.image(img)
    oldfen = board.fen()
    newfen = oldfen
    print (oldfen)
    while oldfen == newfen:
        ig.grab_to_file('/tmp/ss.png')
        img = cv2.imread ('/tmp/ss.png')
        board.image(img)
        newfen = board.fen()


'''
board.move('a2a4')
board.move('b2b4')
board.move('c2c4')
board.move('d2d4')
board.move('e2e4')
board.move('f2f4')
board.move('g2h4')
board.move('h2g4')
'''

'''
while True:
    ig.grab_to_file('/tmp/ss.png')
    img = cv2.imread ('/tmp/ss.png')
    print (board.image(img))

    print (board.fen())
    print ('\n\n')
    time.sleep(1)
'''

