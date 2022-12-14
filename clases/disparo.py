import pygame

class Misil(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.imagenMisil = pygame.image.load("imagenes/misil.png")
        self.rect = self.imagenMisil.get_rect()
        self.velocidadDisparo = 1
        self.rect.bottom = posY
        self.rect.centerx = posX

    def recorrido(self):
        self.rect.top = self.rect.top - self.velocidadDisparo

    def dibujar(self, superficie):
        superficie.blit(self.imagenMisil, self.rect)