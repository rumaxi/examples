from pystockfish import *


class Stockfish:
    def __init__(self):
        self.engine = Engine(depth = 10)

    def getmove(self,fen):
        self.engine.setfenposition(fen)
        return self.engine.bestmove()
