#!/usr/bin/python
#-*- coding: utf-8 -*-
from code.Entity import Entity


# Criando Level:
class Level:
    def __init__(self, screen, name, menu_return):
        self.screen = screen
        self.name = name
        self.mode = menu_return
        self.entity_List: list[Entity] = []

    def run(self, ):
        pass

