#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.key

from code.Constante import ENTITY_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, ENTITY_SHOOT_DELAY
from code.Entity import Entity
from code.PlayerShoot import PlayerShoot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:  # Se tecla seta para cima foi pressionada.
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[
            self.name]] and self.rect.bottom < SCREEN_HEIGHT:  # Se tecla seta para baixo foi pressionada.
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[
            PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:  # Se tecla seta para esquerda foi pressionada.
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[
            self.name]] and self.rect.right < SCREEN_WIDTH:  # Se tecla seta para direita foi pressionada.
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.shoot_delay = ENTITY_SHOOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShoot(f'{self.name}Shoot', (self.rect.centerx,self.rect.centery))
            else:
                return None
        else:
            return None
