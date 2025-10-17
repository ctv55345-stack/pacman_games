import pygame
from .constants import *

class Player:
    def __init__(self):
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.direction = PLAYER_START_DIRECTION
        self.speed = PLAYER_SPEED
        self.counter = 0
        self.images = []
        self.load_images()
        
    def load_images(self):
        for i in range(1, 5):
            self.images.append(pygame.transform.scale(
                pygame.image.load(f'{ASSET_PATHS["player_images"]}{i}.png'), (45, 45)))
    
    def get_center(self):
        return self.x + 23, self.y + 24
    
    def draw(self, screen, flicker):
        center_x, center_y = self.get_center()
        if self.direction == 0:
            screen.blit(self.images[self.counter // 5], (self.x, self.y))
        elif self.direction == 1:
            screen.blit(pygame.transform.flip(self.images[self.counter // 5], True, False), (self.x, self.y))
        elif self.direction == 2:
            screen.blit(pygame.transform.rotate(self.images[self.counter // 5], 90), (self.x, self.y))
        elif self.direction == 3:
            screen.blit(pygame.transform.rotate(self.images[self.counter // 5], 270), (self.x, self.y))
    
    def check_position(self, level):
        center_x, center_y = self.get_center()
        turns = [False, False, False, False]
        num1 = (HEIGHT - 50) // 32
        num2 = (WIDTH // 30)
        num3 = 15
        
        if center_x // 30 < 29:
            if self.direction == 0:
                if level[center_y // num1][(center_x - num3) // num2] < 3:
                    turns[1] = True
            if self.direction == 1:
                if level[center_y // num1][(center_x + num3) // num2] < 3:
                    turns[0] = True
            if self.direction == 2:
                if level[(center_y + num3) // num1][center_x // num2] < 3:
                    turns[3] = True
            if self.direction == 3:
                if level[(center_y - num3) // num1][center_x // num2] < 3:
                    turns[2] = True

            if self.direction == 2 or self.direction == 3:
                if 12 <= center_x % num2 <= 18:
                    if level[(center_y + num3) // num1][center_x // num2] < 3:
                        turns[3] = True
                    if level[(center_y - num3) // num1][center_x // num2] < 3:
                        turns[2] = True
                if 12 <= center_y % num1 <= 18:
                    if level[center_y // num1][(center_x - num2) // num2] < 3:
                        turns[1] = True
                    if level[center_y // num1][(center_x + num2) // num2] < 3:
                        turns[0] = True
            if self.direction == 0 or self.direction == 1:
                if 12 <= center_x % num2 <= 18:
                    if level[(center_y + num1) // num1][center_x // num2] < 3:
                        turns[3] = True
                    if level[(center_y - num1) // num1][center_x // num2] < 3:
                        turns[2] = True
                if 12 <= center_y % num1 <= 18:
                    if level[center_y // num1][(center_x - num3) // num2] < 3:
                        turns[1] = True
                    if level[center_y // num1][(center_x + num3) // num2] < 3:
                        turns[0] = True
        else:
            turns[0] = True
            turns[1] = True

        return turns
    
    def move(self, turns_allowed):
        if self.direction == 0 and turns_allowed[0]:
            self.x += self.speed
        elif self.direction == 1 and turns_allowed[1]:
            self.x -= self.speed
        if self.direction == 2 and turns_allowed[2]:
            self.y -= self.speed
        elif self.direction == 3 and turns_allowed[3]:
            self.y += self.speed
        
        if self.x > WIDTH:
            self.x = -47
        elif self.x < -50:
            self.x = 897
    
    def reset(self):
        self.x = PLAYER_START_X
        self.y = PLAYER_START_Y
        self.direction = PLAYER_START_DIRECTION
        self.counter = 0
