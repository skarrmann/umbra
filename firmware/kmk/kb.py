import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import KeysScanner

_KEY_CFG = [
    board.GP0,  board.GP1,  board.GP2,  board.GP3,  board.GP4,  board.GP21, board.GP22, board.GP26, board.GP27, board.GP28,
    board.GP8,  board.GP7,  board.GP6,  board.GP5,                          board.GP20, board.GP19, board.GP18, board.GP17,
                            board.GP9,  board.GP10, board.GP11, board.GP12, board.GP13, board.GP14,
]

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        self.matrix = KeysScanner(_KEY_CFG)
