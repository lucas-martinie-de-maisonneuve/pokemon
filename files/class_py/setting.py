import pygame
from files.class_py.element import Element
from files.class_py.screen import Screen

class Setting(Element,Screen):
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)

        self.setting_run = False

    def setting(self):
        d = 1
        while self.setting_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    #self.detail_setting = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d: #and not self.detail_setting:
                        pass
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_q: #and self.detail_setting:
                        if d > 0:
                            d -= 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_z: #and not self.detail_setting:
                        if d > 0:
                            d -= 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s: #and not self.detail_setting:
                        if d < 5:
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
                        elif d == 4:
                            pass
                            # Logique pour l'option 4
                    elif event.key == pygame.K_ESCAPE:
                        self.setting_run = False
                
                self.img(525, 350, 1244, 700, 'menu/backgroundmenu')
                self.img(200, 550, 100, 100, 'menu/play')
                self.texte(16,'Play',(0,0,0),200,620)
                         
                self.img(800, 550, 100, 100, 'menu/add_poke')
                self.texte(16,'Add Pokemon',(0,0,0),800,620) 
                self.img(990, 60, 80, 80, 'menu/settings')
                self.texte(14,'Settings',(0,0,0),990,110)     
                self.draw_overlay(200)
                
                self.button_rect((150, 140, 130),525,350,830,560) #Bloc Principal Parametre
                self.button_rect((100,100,100),205,350,170,350) #Bloc Menu
                self.simple_rect(self.black,615,350,610,500,2) #Bordure Détails

                #Coch    
                if d == 0:
                    self.img(140,100,46,46,"/setting/croix_jaune")

                else:
                    self.img(140,100,46,46,"/setting/croix_rouge")
                # Selecteur 1
                if d == 1:
                    self.button_rect((160, 160, 160), 205, 220, 160, 40)  # Boutton selectionné
                    
                    #Touche Echap
                    self.img(500,250,50,50,"/setting/key_echap")
                    self.texte(15,"Retour",self.black,500,280)
                    self.texte(15,"Quitter",self.black,500,300)

                    #Touche Entrée
                    self.img(720,240,70,70,"/setting/key_return")
                    self.texte(15,"Selectionné",self.black,720,280)

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
                    self.button_rect((70, 70, 70), 205, 220, 160, 40)  # Couleur de base
                self.texte(15, 'Controles', (0, 0, 0), 205, 220)

                # Selecteur 2
                if d == 2:
                    self.button_rect((160, 160, 160), 205, 307, 160, 40)
                    
                else:
                    self.button_rect((70, 70, 70), 205, 307, 160, 40)
                self.texte(15, 'Audio', (0, 0, 0), 205, 307)

                # Selecteur 3
                if d == 3:
                    self.button_rect((160, 160, 160), 205, 394, 160, 40)
                else:
                    self.button_rect((70, 70, 70), 205, 394, 160, 40)
                self.texte(15, 'Compte', (0, 0, 0), 205, 394)

                # Selecteur 4
                if d == 4:
                    self.button_rect((160, 160, 160), 205, 481, 160, 40)
                else:
                    self.button_rect((70, 70, 70), 205, 481, 160, 40)
                self.texte(15, '...', (0, 0, 0), 205, 481)
                self.img(205,576,150,150,"/setting/pikachu")
                self.update()
