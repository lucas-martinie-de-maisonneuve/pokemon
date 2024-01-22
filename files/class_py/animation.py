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
                self.img_pokeball(725, 249, 60,60, 'starter/pokeball', self.x)
                self.x += 5
                if self.x == 45:
                    right = False
            elif left == True:
                self.img_pokeball(725, 249, 60,60, 'starter/pokeball', self.x)
                self.x -= 5
                if self.x == -45:
                    left = False
            elif right == False and left == False:
                self.delai()
                self.anim_pokeball()
            self.update_no_fill()

    def pokeball_move(self):
        pokeball_throw = True
        poke_x, poke_y = 0, 540
        mv1, mv2, mv3, mv4, mv5 = True, True, True, True, True

        while pokeball_throw:
            if mv1 == True:
                self.img_pokeball(poke_x, poke_y, 60,60, 'starter/pokeball', -20)
                poke_x += 5
                poke_y -= 5
                self.animation_update()
                if poke_x == 340 and poke_y == 200:
                    mv1 = False
            elif mv2 == True:
                self.img_pokeball(poke_x, poke_y, 60,60, 'starter/pokeball', -20)
                poke_x += 5
                poke_y -= 3
                self.animation_update()
                if poke_x == 500 and poke_y == 104:
                    mv2 = False
            elif mv3 == True:
                self.img_pokeball(poke_x, poke_y, 60,60, 'starter/pokeball', -20)
                poke_x += 5
                self.animation_update()
                if poke_x == 650:
                    mv3 = False
            elif mv4 == True:
                self.img_pokeball(poke_x, poke_y, 60,60, 'starter/pokeball', -20)
                poke_x += 5
                poke_y += 5
                self.animation_update()
                if poke_x == 725 and poke_y == 179:
                    mv4 = False
            elif mv5 == True:
                self.img_pokeball(poke_x, poke_y, 60,60, 'starter/pokeball', -20)
                poke_y += 5
                self.animation_update()
                if poke_y == 249:
                    mv5 = False
            elif poke_x == 725 and poke_y == 249:
                self.anim_pokeball()
        