#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Constante import SCREEN_WIDTH, SCREEN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    def Run(self):
        while True:
            menu = Menu(self.screen)
            menu.Run()

