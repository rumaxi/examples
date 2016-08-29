import cv2
import sys
import numpy as np
import pyautogui as gui

class Board():
    THRESHOLD = 0.8
    asset = {       'ul':   'assets/upper_left.png',
                    'br':   'assets/bottom_right_3.png',
                    'check':'assets/check.png',
             }

    piece_asset = { 'p': 'assets/pawn_b.png',
                    'r': 'assets/rook_b.png',
                    'n': 'assets/knight_b.png',
                    'k': 'assets/king_b.png',
                    'q': 'assets/queen_b.png',
                    'b': 'assets/bishop_b.png',
                    'P': 'assets/pawn_w.png',
                    'R': 'assets/rook_w.png',
                    'N': 'assets/knight_w.png',
                    'K': 'assets/king_w_1.png',
                    'Q': 'assets/queen_w.png',
                    'B': 'assets/bishop_w_1.png',
                    }
    piece           = {}
    ''' 
    board_h     = None
    board_w     = None
    board_ul    = None
    board_br    = None
    cell_h      = None
    cell_w      = None
    x_offset    = None
    y_offset    = None
    board_img   = None
    board_bw    = None
    '''  

    def __init__(self):
        for symbol, filename in self.piece_asset.items():
            self.piece[symbol] = cv2.imread (filename, cv2.IMREAD_GRAYSCALE)

    def image(self, image):
        image_bw    = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        tmpl        = cv2.imread(self.asset['check'], cv2.IMREAD_GRAYSCALE)
        tmpl_match  = cv2.matchTemplate(image_bw, tmpl ,cv2.TM_CCOEFF_NORMED)
        nres        = np.where (tmpl_match >= 0.90)

        if len(nres[0]):
            ul          = cv2.imread(self.asset['ul'], cv2.IMREAD_GRAYSCALE)
            br          = cv2.imread(self.asset['br'], cv2.IMREAD_GRAYSCALE)
            ul_match    = cv2.matchTemplate(image_bw, ul ,cv2.TM_CCOEFF_NORMED)
            ul_coord    = cv2.minMaxLoc(ul_match)[3]
            ul_h, ul_w  = ul.shape
            self.board_ul = (ul_coord[0] +  2, ul_coord[1] + 2) # MAGIC 2px white border

            br_match    = cv2.matchTemplate(image_bw, br, cv2.TM_CCOEFF_NORMED)
            br_coord    = cv2.minMaxLoc(br_match)[3]
            br_h, br_w  = br.shape

            self.board_br = (br_coord[0] + br_h - 3, br_coord[1] + br_w - 3) # MAGIC 2px white border
            (self.x_offset, self.y_offset)  = ul_coord
            self.board_h, self.board_w      = self.board_br[1] - self.y_offset, self.board_br[0] - self.x_offset

            self.cell_h, self.cell_w        = self.board_h/8, self.board_w/8
            self.board_img = image[self.y_offset:self.y_offset+self.board_h,self.x_offset:self.x_offset+self.board_w]
            self.board_bw = cv2.cvtColor(self.board_img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite ('cut.png',self.board_bw)
            return (self.board_ul + self.board_br)
        else:
            return None

    def fen(self):
        fenboard = ''
        for cell_px in range(0,8):
            for cell_py in range(0,8):
                cell_y, cell_dy = cell_py*self.cell_h, (cell_py+1)*self.cell_h
                cell_x, cell_dx = cell_px*self.cell_h, (cell_px+1)*self.cell_h
                cell = self.board_bw[cell_x:cell_dx, cell_y:cell_dy]
                #cv2.imwrite('cell'+str(cell_px)+str(cell_py)+'.png', cell)
                sym = ''
                for symbol, img in self.piece.items():
                    match = cv2.matchTemplate(cell, img ,cv2.TM_CCOEFF_NORMED)
                    nres = np.where (match >= self.THRESHOLD) 
                    if len(nres[0]):
                        sym = symbol
                if not (sym):
                    sym = '1'
                fenboard += sym
            fenboard += '/'

        fenresult   = ''
        spaces      = 0 
        for i in range(len(fenboard)):
            if fenboard[i] != '1':
                if fenboard[i-1] == '1':
                    fenresult += str(spaces)
                    spaces = 0
                fenresult += fenboard[i]
            else:
                spaces = spaces + 1

        return (fenresult)

    def move(self, move):
        print (move)
        f_cell_x, f_cell_y, t_cell_x, t_cell_y = tuple(move)
        f_cell_x = ord(f_cell_x)-96 # ord(a)=97
        t_cell_x = ord(t_cell_x)-96 

        f_x = f_cell_x * self.cell_w + self.x_offset - float(0.5) * self.cell_w
        t_x = t_cell_x * self.cell_w + self.x_offset - float(0.5) * self.cell_w

        f_y = self.y_offset + self.board_h - int(f_cell_y) * self.cell_h + 0.5 * int(self.cell_h)
        t_y = self.y_offset + self.board_h - int(t_cell_y) * self.cell_h + 0.5 * int(self.cell_h)

        gui.moveTo((f_x,f_y))
        gui.dragTo(t_x, t_y, button='left') 




if __name__ == '__main__':
    pass

