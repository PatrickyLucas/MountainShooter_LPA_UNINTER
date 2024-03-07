#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Constante import SCREEN_WIDTH


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surface = pygame.image.load('./asset/menuBg.png')
        self.rect = self.surface.get_rect(left=0, top=0)

    def Run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.screen.blit(source=self.surface, dest=self.rect)
            self.menu_text(text_size=50, text='Mountain', text_color=(255, 128, 0),
                           text_center_position=((SCREEN_WIDTH / 2), 70))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surface.get_rect(center=text_center_position)
        self.screen.blit(source=text_surface, dest=text_rect)
