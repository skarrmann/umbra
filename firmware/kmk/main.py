from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

layers_ext = Layers()

keyboard.modules = [layers_ext]

P1 = KC.DF(0)
P2 = KC.DF(1)
FUN = KC.MO(2)

keyboard.keymap = [
    [ # Player 1
        KC.A   , KC.B   , KC.C   , KC.D   , KC.E   ,                   KC.F   , KC.G   , KC.H   , KC.I   , KC.J   ,
        KC.K   , KC.L   , KC.M   , KC.N   ,                                     KC.O   , KC.P   , KC.Q   , KC.R   ,
                                   KC.S   , KC.T   , KC.U   , KC.V   , KC.W   , FUN    ,
    ],
    [ # Player 2
        KC.N1  , KC.N2  , KC.N3  , KC.N4  , KC.N5  ,                   KC.N6  , KC.N7  , KC.N8  , KC.N9  , KC.N0  ,
        KC.LEFT, KC.DOWN, KC.UP  , KC.RGHT,                                     KC.COMM, KC.DOT , KC.MINS, KC.EQL ,
                                   KC.QUOT, KC.LBRC, KC.RBRC, KC.BSLS, KC.SLSH, FUN    ,
    ],
    [ # Function
        KC.NO  , KC.NO  , KC.NO  , KC.NO  , P1     ,                   P2     , KC.NO  , KC.NO  , KC.NO  , KC.NO  ,
        KC.NO  , KC.NO  , KC.NO  , KC.NO  ,                                     KC.NO  , KC.NO  , KC.NO  , KC.NO  ,
                                   KC.NO  , KC.NO  , KC.NO  , KC.NO  , KC.NO  , FUN    ,
    ],
]

if __name__ == '__main__':
    keyboard.go()
