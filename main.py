import os
import sys
import pygame
import random

pygame.init()
size = width, height = 600, 300
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = "data/" + name
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert
    return image


class Landing(pygame.sprite.Sprite):
    image = load_image("pt.jpg", -1)

    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = Landing.image
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        # если ещё в небе
        if not pygame.sprite.collide_mask(self, mountain):
            self.rect = self.rect.move(0, 1)


class Mountain(pygame.sprite.Sprite):
    image = load_image("mountain.png", -1)

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Mountain.image
        self.image = pygame.transform.scale(self.image, (600, 300))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.bottom = height

mountain = Mountain()
while True:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            Landing(event.pos)
    all_sprites.draw(screen)
    all_sprites.update()
    clock.tick(100)
    pygame.display.flip()
