import pygame
from files.class_py.element import Element
from files.class_py.screen import Screen
from files.class_py.pokedex import Pokedex

class Setting(Element,Screen):
    def __init__(self):
        Element.__init__(self)
        Screen.__init__(self)
        self.verif_quitter = False
        self.setting_run = False
        self.verif_reset = False
        self.reset = False

    def setting(self):
        pokedex = Pokedex()
        m = 1
        c_quit = 1
        c_stat = 0
        c_verif_quit = 1
        c_verif_reset = 1
        c_audio = 0
        pourcent = 0
        self.top_pokemon = sorted(pokedex.pkmn_rencontre,key=lambda x: x['rencontre'], reverse=True)
        pokedex = Pokedex()
        if self.setting_run:
            pokedex.print_pkmn()
        while self.setting_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
#Touche Gauche
                    if event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        #Gauche verif quit
                        if self.verif_quitter and c_verif_quit == 2:
                            c_verif_quit = 1
                        #Gauche stat
                        elif m == 2 and c_stat > 0:
                            c_stat -= 1
                        #Gauche reset
                        if self.verif_reset and c_verif_reset == 2:
                            c_verif_reset = 1
#Touche Droite
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        #Droite vérif quitter
                        if self.verif_quitter and c_verif_quit == 1:
                            c_verif_quit = 2
                        #Droite stat
                        elif m == 2 and c_stat < 1:
                            c_stat += 1
                        # Droite reset
                        if self.verif_reset and c_verif_reset == 1:
                            c_verif_reset = 2
#Touche Haut
                    elif event.key == pygame.K_UP or event.key == pygame.K_z:
                        #menu haut
                        if not self.verif_quitter and not self.verif_reset and m > 0:
                            m -= 1
#Touche Bas
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        #menu bas
                        if not self.verif_quitter and not self.verif_reset and m < 4:
                            m += 1
#Touche Entrée
                    elif event.key == pygame.K_RETURN:
                        #Croix exit setting
                        if m == 0:
                            self.setting_run = False
                        #Lance la fonction "voulez vous vraiment quitter"
                        elif m == 4 and not self.verif_quitter and not self.verif_reset:
                            self.verif_quitter = True
                        #Action à "non" à "voulez vous vraiment quitter"
                        elif c_verif_quit == 1 and self.verif_quitter:
                            self.verif_quitter = False
                        #Action à "oui" à "voulez vous vraiment quitter"
                        elif c_verif_quit == 2 :
                            pygame.quit()
                            quit()
                        #Vérification reset
                        elif c_stat == 1 and m == 2 and not self.verif_reset:
                            self.verif_reset = True
                        #Action à "non" au reset
                        elif c_verif_reset == 1 and self.verif_reset:
                            self.verif_reset = False
                        #Action à "oui" au reset 
                        elif c_verif_reset == 2 and self.verif_reset:
                            pokedex.vider_fichier_json()
                            self.top_pokemon = sorted(pokedex.pkmn_rencontre,key=lambda x: x['rencontre'], reverse=True)
                            self.verif_reset = False
                            self.reset = True

#Touche Echap
                    #Quitter les paramètre 
                    elif event.key == pygame.K_ESCAPE and not self.verif_quitter and not self.verif_reset:
                        self.setting_run = False
                    #Quitter verif_quitter 
                    elif event.key == pygame.K_ESCAPE and self.verif_quitter :
                        self.verif_quitter = False
                        c_verif_quit = 1
                    #Quitter verif_reset
                    elif event.key == pygame.K_ESCAPE and self.verif_reset :
                        self.verif_reset = False
                        c_verif_reset = 1

                self.img(525, 350, 1244, 700, 'menu/backgroundmenu')
                self.img(990, 60, 80, 80, 'menu/settings')
                self.draw_overlay((0,0,0,200), 525,350, self.W, self.H)
                self.texte(14,'Settings',self.black,990,110)     
                
                self.button_rect(self.grey,525,350,830,560) #Bloc Principal Parametre
                
                self.button_rect(self.darkgreenblue,205,350,170,350) #Bloc Menu
                self.simple_rect(self.black,205,350,170,350,2) #Bordure Menu

                self.button_rect(self.greyblue,615,350,610,500) #Bloc Détails
                self.simple_rect(self.black,615,350,610,500,2) #Bordure Détails

                #Croix exit
                if m == 0:
                    self.img(140,100,46,46,"/setting/croix_jaune")
                    self.img(205,576,150,150,"/setting/pikachu_sleep")
                else:
                    self.img(140,100,46,46,"/setting/croix_rouge")

                # Selecteur 1 Controles
                if m == 1:
                    self.button_rect(self.lightbluesea, 205, 220, 160, 40)  # Boutton selectionné
                    
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
                    self.button_rect(self.darkgreenblue, 205, 220, 160, 40)  # Couleur de base
                    self.img(205,576,150,150,"/setting/pikachu_sleep")
                self.texte(15, 'Controles', self.white, 205, 220)

                # Selecteur 2 Statistiques/Reset
                if m == 2 and not self.verif_reset:
                    self.button_rect(self.lightbluesea, 205, 307, 160, 40)
                    self.img(205,576,150,150,"/setting/pikachu_awake")

                    # Statistiques parties pokemon
                    self.texte_not_align(15,f"Nombre de pokemon rencontré: {len(pokedex.pkmn_rencontre)}/{pokedex.get_last_pokemon_number()}", self.black,320,130)
                    self.texte_not_align(15,f"Nombre de combat gagné: ", self.black,320,180)
                    self.texte_not_align(15,f"Nombre de fuite: ", self.black,320,230)
                    self.texte_not_align(15,f"Pokemon les plus rencontres:", self.black,320, 340)
                    if self.top_pokemon:
                        self.texte_not_align(15, f"Dernier pokemon découvert: {pokedex.pkmn_rencontre[-1]['nom']}", self.black, 320, 280)

                        self.button_rect(self.black,430, 560, 150,50)#cadre noir titre nom
                        self.button_rect(self.lightgrey,430, 475, 150,150) #cadre gris clair pokemon
                        self.img(430, 475, 150,150,f"/pokemon/{self.top_pokemon[0]['nom'].lower()}") #img pokemon
                        self.texte(15, f"(x{self.top_pokemon[0]['rencontre']})", self.black,470, 540) #nombre de fois rencontrer
                        self.texte(15, f"{self.top_pokemon[0]['nom']}", self.white,430, 565) #nom pokemon dans cadre noir

                        if len(self.top_pokemon) > 1:
                            self.button_rect(self.black,620, 560, 150,50)
                            self.button_rect(self.lightgrey,620, 475, 150,150)
                            self.img(620, 475, 150,150,f"/pokemon/{self.top_pokemon[1]['nom'].lower()}")
                            self.texte(15, f"(x{self.top_pokemon[1]['rencontre']})", self.black,660, 540) 
                            self.texte(15, f"{self.top_pokemon[1]['nom']}", self.white,620, 565) 
                        else:
                            self.texte_not_align(15, f"Aucun", self.black, 640, 340)
                        if len(self.top_pokemon) > 2:
                            self.button_rect(self.black,810, 560, 150,50)
                            self.button_rect(self.lightgrey,810, 475, 150,150)
                            self.img(810, 475, 150,150,f"/pokemon/{self.top_pokemon[2]['nom'].lower()}")
                            self.texte(15, f"(x{self.top_pokemon[2]['rencontre']})", self.black,850, 540) 
                            self.texte(15, f"{self.top_pokemon[2]['nom']}", self.white,810, 565) 
                        else:
                            self.texte_not_align(15, f"Aucun", self.black, 640, 320)
                    else: 
                        self.texte_not_align(15, f"Dernier pokemon découvert: Aucun", self.black, 320, 280)
                        self.texte_not_align(15, f"Aucun", self.black, 640, 340)

                    if c_stat == 1:
                        self.button_rect(self.darkbluesea,880,140,50,50)
                        self.img_mir(880,140,30,30,"/setting/logo_reset")

                    else:
                        self.button_rect(self.darkgreenblue,880,140,50,50)
                        self.img_mir(880,140,30,30,"/setting/logo_reset")
                else:
                    self.button_rect((37, 50, 55), 205, 307, 160, 40)
                self.texte(15, 'Statistiques', self.white, 205, 307)

                # Selecteur 3 Audio
                if m == 3:
                    self.img(205,576,150,150,"/setting/pikachu_music")
                    self.button_rect(self.lightbluesea, 205, 394, 160, 40)
                    self.button_rect(self.lightgrey,570,170,450,60) #Barre de son
                    
                    if c_audio == 2:
                        pass
                    else:
                        self.button_rect(self.lightgrey,860,170,60,60) #Bouton Mute

                else:
                    self.button_rect(self.darkgreenblue, 205, 394, 160, 40)
                self.texte(15, 'Audio', self.white, 205, 394)

                # Selecteur 4 Quitter
                if m == 4:
                    self.button_rect((39, 76, 119), 205, 481, 160, 40)
                    self.img(205,576,150,150,"/setting/pikachu_angry")
                    self.button_rect(self.lightgrey,615,350,500,200)
                    self.simple_rect(self.black,615,350,500,200,2)
                    self.texte(18,"Quitter le jeu",self.black,615,340)

                    if  c_quit == 1:
                        self.button_rect(self.darkbluesea,615,400,100,50)
                        self.texte(13,"Oui", self.white,615,400)
                    else:
                        self.button_rect((37, 50, 55),615,400,100,50)
                        self.texte(13,"Oui", self.white,615,400)
                else:
                    self.button_rect((37, 50, 55), 205, 481, 160, 40)
                self.texte(15, 'Quitter', self.white, 205, 481)

                #Affichage verif reset
                if self.verif_reset:
                    self.button_rect(self.lightgrey,615,375,350,350) #Rectangle gris
                    self.button_rect(self.darkbluesea,615,175,350,50) #Rectangle bleu
                    self.texte(20,"Effacer les données",self.white,615,175)
                    self.simple_rect(self.black,615,350,350,400,2) #Bordure
                    self.texte(13,"Les données de sauvergarde de Pokémon seront complétements effacées. Une fois effacées, les données ne pourront plus être utilisées ou récupérées. Voulez vous continuer ?",self.darkgreenblue,700,350)

                    if c_verif_reset == 1:
                        self.button_rect(self.darkbluesea,515,500,70,50)
                        self.texte(13,"Non", self.white,515,500)
                    else:
                        self.button_rect(self.darkgreenblue,515,500,70,50)
                        self.texte(13,"Non", self.white,515,500)
                    
                    if c_verif_reset == 2:
                        self.button_rect(self.darkbluesea, 715,500,70,50)
                        self.texte(13,"Oui", self.white,715,500)
                    else:
                        self.button_rect(self.darkgreenblue,715,500,70,50)
                        self.texte(13,"Oui", self.white,715,500)
                #Affichage verif quitter
                if self.verif_quitter:
                    self.button_rect(self.darkgrey,615,350,500,200)
                    self.simple_rect(self.black,615,350,500,200,2)
                    self.texte(18,"Voulez vous vraiment quitter ?", self.white,615,340)

                    if c_verif_quit == 1:
                        self.button_rect(self.darkbluesea,515,400,70,50)
                        self.texte(13,"Non", self.white,515,400)
                    else:
                        self.button_rect(self.darkgreenblue,515,400,70,50)
                        self.texte(13,"Non", self.white,515,400)
                    
                    if c_verif_quit == 2:
                        self.button_rect(self.darkbluesea, 715,400,70,50)
                        self.texte(13,"Oui", self.white,715,400)
                    else:
                        self.button_rect(self.darkgreenblue,715,400,70,50)
                        self.texte(13,"Oui", self.white,715,400)
                self.update()
