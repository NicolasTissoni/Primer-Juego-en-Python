import pygame
from clases import disparo

class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagenNave = pygame.image.load("imagenes/nave-espacial.png")
        self.imagenExplosion = pygame.image.load("imagenes/explosion.png")

        # Tomo rectangulo imagen
        self.rect = self.imagenNave.get_rect()

        # Posicion inicial de nave
        self.rect.centerx = 200
        self.rect.centery = 590
        self.velocidad = 10
        self.vida = True
        self.listaDisparo = []
        self.SonidoDisparo = pygame.mixer.Sound("sonidos/rayo-laser.wav")

    def mover(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= 448:
                self.rect.right = 448

    def disparar(self, x, y):
        if self.vida == True:
            misil = disparo.Misil(x, y)
            self.listaDisparo.append(misil)
            self.SonidoDisparo.play()

    def dibujar(self, superficie):
        if self.vida == True:
            superficie.blit(self.imagenNave, self.rect)
        else:
            superficie.blit(self.imagenExplosion, self.rect)