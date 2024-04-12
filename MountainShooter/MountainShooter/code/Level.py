#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.display
from pygame import Surface

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

    def run(self, ):
        while True:
            for entity in self.entity_List:
                self.screen.blit(source=entity.surf, dest=entity.rect)
            pygame.display.flip()


