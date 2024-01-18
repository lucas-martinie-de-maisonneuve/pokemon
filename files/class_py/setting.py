import pygame
from files.class_py.element import Element
from files.class_py.screen import Screen
from files.class_py.pokedex import Pokedex

class Setting(Element,Screen,Pokedex):
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
        Pokedex.__init__(self)

        self.verif_quitter = False
        self.setting_run = False

    def setting(self):
        d = 1
        e = 1
        f = 0
        while self.setting_run:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    #self.detail_setting = False
                    if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        if self.verif_quitter and e == 2:
                            e = 1
                        elif f == 1 and d == 4:
                            f = 0
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if not self.verif_quitter and d < 4:
                            pass
                        elif d == 4:
                            f = 1
                        elif self.verif_quitter and e == 1:
                            e = 2
                    elif event.key == pygame.K_UP or event.key == pygame.K_z :
                        if not self.verif_quitter and d > 0:
                            d -= 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if not self.verif_quitter and d < 4:
                            d += 1
                    elif event.key == pygame.K_RETURN:
                        if d == 0:
                            self.setting_run = False
                        elif d == 1:
                            pass
                        elif d == 2:
                            # Logique pour l'option 2
                            pass
                        elif d == 3:
                            # Logique pour l'option 3
                            pass
                        elif f == 1:
                            self.verif_quitter = True
                        if e == 1:
                            self.verif_quitte = False
                            
                        elif e == 2:
                            pygame.quit()
                    elif event.key == pygame.K_ESCAPE and not self.verif_quitter:
                        self.setting_run = False
                    elif event.key == pygame.K_ESCAPE and self.verif_quitter:
                        self.verif_quitter = False
                        e = 1
                    
                
                self.img(525, 350, 1244, 700, 'menu/backgroundmenu')
                self.img(990, 60, 80, 80, 'menu/settings')
                self.texte(14,'Settings',(0,0,0),990,110)     
                self.draw_overlay(200)
                
                self.button_rect((139, 140, 137),525,350,830,560) #Bloc Principal Parametre
                self.button_rect((92, 103, 125),205,350,170,350) #Bloc Menu
                self.simple_rect((self.black),615,350,610,500,2) #Bordure Détails

                #Croix exit
                if d == 0:
                    self.img(140,100,46,46,"/setting/croix_jaune")
                    self.img(205,576,150,150,"/setting/pikachu_sleep")
                else:
                    self.img(140,100,46,46,"/setting/croix_rouge")

                # Selecteur 1
                if d == 1:
                    self.button_rect((39, 76, 119), 205, 220, 160, 40)  # Boutton selectionné
                    
                    #Pikachu
                    self.img(205,576,150,150,"/setting/pikachu_sleep")

                    #Touche Echap
                    self.img(500,250,50,50,"/setting/key_echap")
                    self.texte(15,"Retour",self.black,500,280)
                    self.texte(15,"Quitter",self.black,500,300)

                    #Touche Entrée
                    self.img(720,240,70,70,"/setting/key_return")
                    self.texte(15,"Selectionné",self.black,720,290)

                    #Bloc touche ZQSD
                    self.img(450,450,50,50,"/setting/key_q")
                    self.img(500,450,50,50,"/setting/key_s")
                    self.img(500,400,50,50,"/setting/key_z")
                    self.img(550,450,50,50,"/setting/key_d")

                    #"Ou"
                    self.texte(15,"ou",self.black,610,450)
                    
                    #Bloc touche flèche directionnels
                    self.img(670,450,50,50,"/setting/key_left")
                    self.img(720,450,50,50,"/setting/key_down")
                    self.img(770,450,50,50,"/setting/key_right")
                    self.img(720,400,50,50,"/setting/key_up")
                else:
                    self.button_rect((37, 50, 55), 205, 220, 160, 40)  # Couleur de base
                    self.img(205,576,150,150,"/setting/pikachu_sleep")
                self.texte(15, 'Controles', self.white, 205, 220)

                # Selecteur 2
                if d == 2:
                    self.button_rect((39, 76, 119), 205, 307, 160, 40)
                    self.img(205,576,150,150,"/setting/pikachu_awake")
                    self.texte_not_align(15,f"Nombre de pokemon rencontré: {self.pokemon_counter}", self.black,320,130)
                    self.texte_not_align(15,f"Nombre de combat gagné: {self.info_pokemon}", self.black,320,180)
                    self.texte_not_align(15,f"Nombre de fuite: {self.detailed_pokemon}", self.black,320,230)
                    self.texte_not_align(15,f"Pokemon les plus rencontres:", self.black,320, 280)
                    self.texte_not_align(15,f"{self.rand_pokemon()}:", self.black,620, 300)
                    self.texte_not_align(15,f"{self.rand_pokemon()}", self.black,620, 320)
                    self.texte_not_align(15,f"{self.rand_pokemon()}", self.black,620, 340)

                else:
                    self.button_rect((37, 50, 55), 205, 307, 160, 40)
                self.texte(15, 'Statistiques', self.white, 205, 307)

                # Selecteur 3
                if d == 3:
                    self.button_rect((39, 76, 119), 205, 394, 160, 40)
                    self.img(205,576,150,150,"/setting/pikachu_music")
                else:
                    self.button_rect((37, 50, 55), 205, 394, 160, 40)
                self.texte(15, 'Audio', self.white, 205, 394)

                # Selecteur 4
                if d == 4:
                    self.button_rect((39, 76, 119), 205, 481, 160, 40)
                    self.img(205,576,150,150,"/setting/pikachu_angry")
                    self.button_rect((160, 160, 160),615,350,500,200)
                    self.texte(18,"Quitter le jeu",self.black,615,340)
                    if f == 1:
                        self.button_rect((180, 120, 230),615,400,50,30)
                    else:
                        self.button_rect((37, 50, 55),615,400,50,30)
                    self.texte(13,"Oui", self.white,615,400)
                else:
                    self.button_rect((37, 50, 55), 205, 481, 160, 40)
                self.texte(15, 'Quitter', self.white, 205, 481)




                if self.verif_quitter:
                    self.button_rect((100,100,100),615,350,500,200)
                    self.texte(18,"Voulez vous vraiment quitter ?", self.white,615,340)

                    if e == 1:
                        self.button_rect((39, 76, 119),515,400,50,30)
                        self.texte(13,"Non", self.white,515,400)
                    else:
                        self.button_rect((37, 50, 55),515,400,50,30)
                        self.texte(13,"Non", self.white,515,400)
                    
                    if e == 2:
                        self.button_rect((39, 76, 119), 715,400,50,30)
                        self.texte(13,"Oui", self.white,715,400)
                    else:
                        self.button_rect((37, 50, 55),715,400,50,30)
                        self.texte(13,"Oui", self.white,715,400)
                self.update()
