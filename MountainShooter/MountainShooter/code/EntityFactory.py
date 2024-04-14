#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Constante import SCREEN_WIDTH, SCREEN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for image in range(7):
                    list_bg.append(Background(f'Level1Bg{image}', position))
                    list_bg.append(Background(f'Level1Bg{image}', (SCREEN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, SCREEN_HEIGHT/2 - 30))
            case 'Player2':
                return Player('Player2', (10, SCREEN_HEIGHT/2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (SCREEN_WIDTH+10, random.randint(40, SCREEN_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (SCREEN_WIDTH+10, random.randint(40, SCREEN_HEIGHT - 40)))