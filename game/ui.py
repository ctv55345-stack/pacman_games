import pygame
from .constants import *

class UI:
    def __init__(self):
        self.font = pygame.font.Font(ASSET_PATHS['font'], 20)
        
    def draw_misc(self, screen, score, powerup, lives, game_over, game_won):
        score_text = self.font.render(f'Score: {score}', True, 'white')
        screen.blit(score_text, (10, 920))
        if powerup:
            pygame.draw.circle(screen, 'blue', (140, 930), 15)
        for i in range(lives):
            screen.blit(pygame.transform.scale(pygame.image.load(f'{ASSET_PATHS["player_images"]}1.png'), (30, 30)), (650 + i * 40, 915))
        if game_over:
            pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
            pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
            gameover_text = self.font.render('Game over! Space bar to restart!', True, 'red')
            screen.blit(gameover_text, (100, 300))
        if game_won:
            pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
            pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
            gameover_text = self.font.render('Victory! Space bar to restart!', True, 'green')
            screen.blit(gameover_text, (100, 300))
