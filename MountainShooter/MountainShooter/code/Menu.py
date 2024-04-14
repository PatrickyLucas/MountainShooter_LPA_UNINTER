#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Constante import SCREEN_WIDTH, COLOR_ORANGE, COLOR_WHITE, MENU_OPTION, COLOR_YELLOW

# Criando menu:
class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surface = pygame.image.load('./asset/menuBg.png').convert_alpha()
        self.rect = self.surface.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        menu_option = 0
        while True:
            self.screen.blit(source=self.surface, dest=self.rect)
            self.menu_text(text_size=50, text='Mountain', text_color=COLOR_ORANGE,
                           text_center_position=((SCREEN_WIDTH / 2), 70))
            self.menu_text(text_size=50, text='Shooter', text_color=COLOR_ORANGE,
                           text_center_position=((SCREEN_WIDTH / 2), 120))

            for indice in range(len(MENU_OPTION)):
                if indice == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[indice], text_color=COLOR_YELLOW,
                                   text_center_position=((SCREEN_WIDTH / 2), 200 + 30 * indice))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[indice], text_color=COLOR_WHITE,
                                   text_center_position=((SCREEN_WIDTH / 2), 200 + 30 * indice))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(center=text_center_position)
        self.screen.blit(source=text_surface, dest=text_rect)
