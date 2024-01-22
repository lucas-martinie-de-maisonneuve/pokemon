from files.class_py.element import Element
from files.class_py.screen import Screen


class Animation(Screen, Element):
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
        self.x = 0

    def anim_pokeball(self):
        pokeball_move = True
        left = True
        right = True
        while pokeball_move:
            if right == True: 
                self.img_pokeball(525, 350, 100,100, 'starter/pokeball', self.x)
                self.x += 5
                if self.x == 45:
                    right = False
            elif left == True:
                self.img_pokeball(525, 350, 100,100, 'starter/pokeball', self.x)
                self.x -= 5
                if self.x == -45:
                    left = False
            elif right == False and left == False:
                self.delai()
                self.anim_pokeball()
            self.animation_update()

    def pokeball_move(self):
        pokeball_throw = True
        poke_x, poke_y = 0, 0
        while pokeball_throw:
            self.img_pokeball(poke_x, poke_y, 100,100, 'starter/pokeball', -20)
