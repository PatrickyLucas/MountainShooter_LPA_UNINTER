#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.image
from pygame import Surface


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surface = pygame.image.load('./asset/menuBg.png')
        self.rect = self.surface.get_rect(left=0, top=0)

    def Run(self):
        while True:
            self.screen.blit(source=self.surface, dest=self.rect)
            pygame.display.flip()
        pass

