import pygame
class Screen:
    def __init__(self):
        self.Fenetre = pygame.display.set_mode((1050, 700))
        pygame.display.set_caption("Pokemon")
        self.clock = pygame.time.Clock()

    def update(self):
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(60)
        self.Fenetre.fill((0, 0, 0))


    def get_size(self):
        return self.Fenetre.get_size()

    def get_display(self):
        return self.Fenetre

    def img(self, largeur, hauteur, image_name, x, y):
        image = pygame.image.load(f'image/{image_name}.png')
        image = pygame.transform.scale(image, (largeur, hauteur))
        self.Fenetre.blit(image, (x, y))

