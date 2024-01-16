import pygame
from files.class_py.element import Element
from files.class_py.screen import Screen

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
                        if d > 1:
                            d -= 1
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s and d == 5 and not self.show_home:
                        if d < 4:
                            d += 1
                    elif event.key == pygame.K_RETURN:
                        if d == 1:
                            # Logique pour l'option 1
                            pass
                        elif d == 2:
                            # Logique pour l'option 2
                            pass
                        elif d == 3:
                            # Logique pour l'option 3
                            pass
                        elif d == 4:
                            # Logique pour l'option 4
                            pass

                self.draw_overlay()

    def draw_overlay(self):
        overlay_color = (0, 0, 0, 128) 
        overlay_surface = pygame.Surface((Screen.W, Screen.H), pygame.SRCALPHA)
        overlay_surface.fill(overlay_color)
        Screen.screen.blit(overlay_surface, (0, 0))