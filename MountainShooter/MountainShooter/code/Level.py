#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Constante import COLOR_WHITE, MENU_OPTION, EVENT_ENEMY
from code.Entity import Entity
from code.EntityFactory import EntityFactory


# Criando Level:
class Level:
    def __init__(self, screen, name, menu_return):
        self.screen: Surface = screen
        self.name = name
        self.mode = menu_return
        self.entity_List: list[Entity] = []
        self.entity_List.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_List.append(EntityFactory.get_entity('Player1'))
        if menu_return in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_List.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            for entity in self.entity_List:
                self.screen.blit(source=entity.surf, dest=entity.rect)  # desenhar entidades
                self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, 10))
                entity.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_List.append(EntityFactory.get_entity(choice))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surface: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surface.get_rect(left=text_position[0], top=text_position[1])
        self.screen.blit(source=text_surface, dest=text_rect)
