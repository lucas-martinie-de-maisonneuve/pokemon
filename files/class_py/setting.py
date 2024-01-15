import pygame
from files.class_py.element import Element
from files.class_py.sdreen import Sdreen

class Setting(Element):
    def __init__(self):
        Element.__init__(self)
        self.setting_run = False

    def setting(self):
        d = 0
        while self.setting_run:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.show_home = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if d < 4:
                            d += 1
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_q and not self.show_home:
                        if d > 1:
                            d -= 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_z and not self.show_home:
                        d = 5
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s and d == 5 and not self.show_home:
                        d = 4
                    elif event.key == pygame.K_RETURN:
                        if d == 1:
                            
                                
                            else:
                    elif 

    def daption(self):