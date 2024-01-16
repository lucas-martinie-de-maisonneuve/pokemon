import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element
from files.class_py.pokedex import Pokedex
from files.class_py.combat import Combat
from files.class_py.starter import Starter


pokedex = Pokedex()
class Maps(Element, Screen):

    def __init__(self, poke_player, pokemon_random):
        self.combat_run = True
        self.action = 1
        Element.__init__(self)
        Screen.__init__(self)
        self.combat = Combat()
        self.starter = Starter()               
        self.attack_phase = False
        self.text_phase = False
        self.text = 1
        self.poke_player = poke_player
        self.pokemon_random = pokemon_random
        self.pokemon_random_hp = pokemon_random['hp']
        self.pokemon_type_player = poke_player['type']
        self.type_pokemon_advers = pokemon_random['type']
                

    def home(self):
        while self.combat_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN: 
                    # print('pokeplayer :', poke_player)
                    # print ('pokerandom', pokemon_random)
                    if event.key == pygame.K_RIGHT:
                        if self.action < 4:
                            self.action += 1
                    elif event.key == pygame.K_LEFT:
                        if self.action > 1:
                            self.action -= 1
                    elif event.key == pygame.K_UP and self.action > 2:
                        self.action -= 2
                    elif event.key == pygame.K_DOWN and self.action < 3:
                        self.action += 2
                    elif event.key == pygame.K_RETURN and not self.attack_phase:
                        if self.action == 1:
                            self.attack_phase = True
                        elif self.action == 2 and not self.attack_phase:
                            self.combat_run = False
                        elif self.action == 3 and not self.attack_phase:
                            pass
                        elif self.action == 4 and not self.attack_phase:
                            pokedex.pokedex_run = True
                            pokedex.show_pokedex()
                    elif event.key == pygame.K_RETURN and self.attack_phase:
                        if self.action == 1:
                            self.pokemon_random_hp = self.combat.attack(self.pokemon_random_hp, self.poke_player['attaque'],self.pokemon_type_player,self.type_pokemon_advers)

                        elif self.action == 2 and not self.attack_phase:
                            self.attack_phase = False
                        elif self.action == 3 and not self.attack_phase:
                            self.attack_phase = False
                        elif self.action == 4 and not self.attack_phase:
                            self.attack_phase = False
                    elif event.key == pygame.K_ESCAPE and self.attack_phase:
                        self.attack_phase = False
                            
            self.img(525, 200, 1244, 700,"combat/fight_background")
            self.img_mir(250, 325, 350, 350, f"pokemon/{self.poke_player['nom'].lower()}")                    
            self.img(725, 225, 175, 175, f"pokemon/{self.pokemon_random['nom'].lower()}")
            # combat.afficher_capacite()
            self.button_rect(self.brown,525,650,self.W,210)            
            self.img(300, 625, 470, 150, "combat/background_texte")           
            self.img(850, 625, 399, 150,"combat/zone_texte")

            if not self.attack_phase:
                self.button_rect(self.darkred,765,600,145,45)
                self.simple_rect(self.red,765,600,135,35,2)

                self.button_rect(self.darkblue,945,600,145,45)
                self.simple_rect(self.blue, 945,600,135,35,2)

                self.button_rect(self.darkgreen,765,650,145,45)
                self.simple_rect(self.green, 765,650,135,35,2)

                self.button_rect(self.orange,945,650,145,45)
                self.simple_rect(self.yellow, 945,650,135,35,2)

                if self.action == 1 :
                    self.button_attack = self.texte(19, "ATTACK", self.white, 765, 600)
                    self.img(680, 600, 15, 15, f"combat/arrow")
                else:
                    self.button_attack = self.texte(18, "ATTACK", self.black, 765, 600)
                if self.action == 2 :
                    self.button_run = self.texte(19, "RUN", self.white, 945 , 600)
                    self.img(860, 600, 15, 15, f"combat/arrow")
                else:
                    self.button_run = self.texte(18, "RUN", self.black, 945 , 600)
                if self.action == 3 :
                    self.button_bag = self.texte(19,"ITEMS", self.white, 765, 650)
                    self.img(680, 650, 15, 15, f"combat/arrow")
                else:
                    self.button_bag = self.texte(18,"ITEMS", self.black, 765, 650)
                if self.action == 4 :
                    self.button_pokedex = self.texte(19,"POKEDEX", self.white, 945, 650)
                    self.img(860, 650, 15, 15, f"combat/arrow")
                else:
                    self.button_pokedex = self.texte(18,"POKEDEX", self.black, 945, 650)

            else: 
                self.button_rect(self.white,765,600,145,45)
                self.simple_rect(self.black,765,600,135,35,2)
                self.button_attack = self.texte(16, "Capacité 1", self.black, 765, 600)

                self.button_rect(self.white,945,600,145,45)
                self.simple_rect(self.black, 945,600,135,35,2)
                self.button_run = self.texte(16, "Capacité 2", self.black, 945 , 600)

                self.button_rect(self.white,765,650,145,45)
                self.simple_rect(self.black, 765,650,135,35,2)
                self.button_bag = self.texte(16,"Capacité 3", self.black, 765, 650)

                self.button_rect(self.white,945,650,145,45)
                self.simple_rect(self.black, 945,650,135,35,2)
                self.button_pokedex = self.texte(16,"Capacité 4", self.black, 945, 650)

                if self.action == 1 :
                    self.img(680, 600, 15, 15, f"combat/arrow")
                elif self.action == 2 :
                    self.img(860, 600, 15, 15, f"combat/arrow")
                elif self.action == 3 :
                    self.img(680, 650, 15, 15, f"combat/arrow")
                elif self.action ==4 :
                    self.img(860, 650, 15, 15, f"combat/arrow")

            if self.text_phase:
                self.texte(20, "What do you mean ?", self.black, 300, 625)
            else:
                self.texte(20, f"What will {self.poke_player['nom']} do?", self.black, 300, 625)

            self.update()