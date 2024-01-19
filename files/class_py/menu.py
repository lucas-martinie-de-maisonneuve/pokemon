import pygame
from files.class_py.screen import Screen
from files.class_py.element import Element
from files.class_py.pokedex import Pokedex
from files.class_py.maps_combat import Maps
from files.class_py.combat import Combat
from files.class_py.starter import Starter
from files.class_py.add_pokemon import AddPokemon
from files.class_py.setting import Setting

element = Element()
screen = Screen()
pokedex = Pokedex()
combat = Combat()
starter = Starter()
addpokemon = AddPokemon()
setting = Setting()

class Menu:
    def __init__(self):
        self.menu_run = True
        self.show_home = True
        self.load_home = False

    def home(self):
        c = 1
        d = 1 
        while self.menu_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN and not setting.setting_run:
                    if self.show_home:
                        self.show_home = False
                        self.load_home = True
                        break
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if c < 4:
                            c += 1
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                        if c > 1:
                            c -= 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_z:
                        if d > 1 and self.load_home:
                            d -= 1
                        if c == 3 or c == 4:
                            c = 5
                        elif c == 1 or c == 2:
                            c = 6                        
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if d < 3 and self.load_home:
                            d += 1
                        if c == 5:
                            c = 4
                        elif c == 6:
                            c = 1                   
                    elif event.key == pygame.K_RETURN and self.load_home and not self.show_home:
                        if d == 1 and self.load_home:
                            self.load_home = False
                        if d == 2 and self.load_home:
                            self.load_home = False
                            # + fonction_save
                        if d == 3 and self.load_home:
                            self.menu_run = False
                            self.show_home = False
                            pygame.quit()
                    elif event.key == pygame.K_RETURN and not self.load_home:
                        if c == 1:
                            self.load_home = False
                            if starter.poke_player == "":
                                starter.choose_starter = True
                                starter.starter()
                                pokedex.pokemon_rencontre(starter.poke_player["nom"])
                                pokedex.poke_rencontre(starter.poke_player["nom"])

                            else:
                                pokemon_random = pokedex.rand_pokemon()                           
                                maps = Maps(starter.poke_player,pokemon_random)
                                maps.home()
                                maps.combat_run = True
                                pokedex.pokemon_rencontre(pokemon_random["nom"])
                                pokedex.poke_rencontre(pokemon_random["nom"])

                        elif c == 2:
                            pokedex.pokedex_run = True
                            pokedex.show_pokedex()
                        elif c == 4:
                            addpokemon.ajout_pokemon()
                            pass
                        elif c == 5:
                            setting.setting_run = True
                            setting.setting()
                        elif c == 6:
                            self.load_home = True
                            # = True
                            
            if self.show_home:
                element.img_background(525, 350, 1244, 700, 'background')
                element.img(1000, 650, 70, 70,'pokeball')
                element.img_mir(50, 50, 70,70,'pokeball')
                element.texte(30, 'Appuyer sur une touche pour continuer', (255, 255, 255), screen.W // 2, screen.H // 2)
                screen.update()
                
            
            if self.load_home and not self.show_home:
                element.img(525, 350, 1244, 700, "menu_load/img_background_load")
                if d == 1:
                    element.button_rect(element.black, 525, 200, 300, 80 )
                    element.texte(20, "Nouvelle Partie", element.white, 525, 200)
                else:
                    element.button_rect(element.white, 525, 200, 300, 80 )
                    element.texte(20, "Nouvelle Partie", element.black, 525, 200)
                    
                if d == 2:
                    element.button_rect(element.black, 525, 400, 300, 80 )
                    element.texte(20, "Charger une partie", element.white, 525, 400)
                else:
                    element.button_rect(element.white, 525, 400, 300, 80 )
                    element.texte(20, "Charger une partie", element.black, 525, 400)
                    
                if d == 3:
                    element.button_rect(element.black, 525, 600, 300, 80  )
                    element.texte(20, "Quitter le jeu", element.white, 525, 600)
                else:
                    element.button_rect(element.white, 525, 600, 300, 80 )
                    element.texte(20, "Quitter le jeu", element.black, 525, 600)                                    
                screen.update()
                                

            if not self.show_home and not self.load_home:      
                element.img(525, 350, 1244, 700, 'menu/backgroundmenu')
                if starter.poke_player != "":
                    element.img(525, 250, 400, 400, f'pokemon/{starter.poke_player["nom"].lower()}')

                if c == 1 : 
                    element.img(200, 550, 120, 120, 'menu/play')
                    element.texte(20,'Play',(255,255,255),200,630)
                else:
                    element.img(200, 550, 100, 100, 'menu/play')
                    element.texte(16,'Play',(0,0,0),200,620)
                if c == 2:
                    element.img(400, 550, 120, 120, 'menu/pokedex')
                    element.texte(20,'Pokedex',(255,255,255),400,630)
                else:
                    element.img(400, 550, 100, 100, 'menu/pokedex')
                    element.texte(16,'Pokedex',(0,0,0),400,620)
                if c == 3:
                    element.img(600, 550, 120, 120, 'menu/bag')
                    element.texte(20,'Bag',(255,255,255),600,630)
                else: 
                    element.img(600, 550, 100, 100, 'menu/bag')
                    element.texte(16,'Bag',(0,0,0),600,620)
                if c == 4:                 
                    element.img(800, 550, 120, 120, 'menu/add_poke')
                    element.texte(20,'Add Pokemon',(255,255,255),800,630)
                else:
                    element.img(800, 550, 100, 100, 'menu/add_poke')
                    element.texte(16,'Add Pokemon',(0,0,0),800,620)
                if c == 5:
                    element.img(990, 60, 100, 100, 'menu/settings')
                    element.texte(17,'Settings',(255,255,255),990,120)
                else:
                    element.img(990, 60, 80, 80, 'menu/settings')
                    element.texte(14,'Settings',(0,0,0),990,110)
                    
                if c == 6:
                    element.img(30, 30, 53, 53, "setting/croix_rouge")                
                else:
                    element.img(30, 30, 46, 46, "setting/croix_rouge")
                screen.update()