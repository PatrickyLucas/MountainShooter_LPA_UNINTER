#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Constante import SCREEN_WIDTH


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
