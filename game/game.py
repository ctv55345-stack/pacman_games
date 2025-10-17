import pygame
import copy
from .constants import *
from .player import Player
from .ghost import Ghost
from .board import Board
from .ui import UI

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.timer = pygame.time.Clock()
        self.player = Player()
        self.board = Board()
        self.ui = UI()
        
        self.direction_command = 0
        self.counter = 0
        self.flicker = False
        self.score = SCORE_START
        self.powerup = False
        self.power_counter = 0
        self.eaten_ghost = [False, False, False, False]
        self.targets = [(self.player.x, self.player.y), (self.player.x, self.player.y), (self.player.x, self.player.y), (self.player.x, self.player.y)]
        
        self.blinky_x = BLINKY_START_X
        self.blinky_y = BLINKY_START_Y
        self.blinky_direction = BLINKY_START_DIRECTION
        self.inky_x = INKY_START_X
        self.inky_y = INKY_START_Y
        self.inky_direction = INKY_START_DIRECTION
        self.pinky_x = PINKY_START_X
        self.pinky_y = PINKY_START_Y
        self.pinky_direction = PINKY_START_DIRECTION
        self.clyde_x = CLYDE_START_X
        self.clyde_y = CLYDE_START_Y
        self.clyde_direction = CLYDE_START_DIRECTION
        
        self.blinky_dead = False
        self.inky_dead = False
        self.clyde_dead = False
        self.pinky_dead = False
        self.blinky_box = False
        self.inky_box = False
        self.clyde_box = False
        self.pinky_box = False
        
        self.moving = False
        self.ghost_speeds = GHOST_SPEEDS.copy()
        self.startup_counter = 0
        self.lives = LIVES_START
        self.game_over = False
        self.game_won = False
        
        self.load_assets()
        
    def load_assets(self):
        self.blinky_img = pygame.transform.scale(pygame.image.load(f'{ASSET_PATHS["ghost_images"]}{GHOST_IMAGES["blinky"]}'), (45, 45))
        self.pinky_img = pygame.transform.scale(pygame.image.load(f'{ASSET_PATHS["ghost_images"]}{GHOST_IMAGES["pinky"]}'), (45, 45))
        self.inky_img = pygame.transform.scale(pygame.image.load(f'{ASSET_PATHS["ghost_images"]}{GHOST_IMAGES["inky"]}'), (45, 45))
        self.clyde_img = pygame.transform.scale(pygame.image.load(f'{ASSET_PATHS["ghost_images"]}{GHOST_IMAGES["clyde"]}'), (45, 45))
        self.spooked_img = pygame.transform.scale(pygame.image.load(f'{ASSET_PATHS["ghost_images"]}{GHOST_IMAGES["spooked"]}'), (45, 45))
        self.dead_img = pygame.transform.scale(pygame.image.load(f'{ASSET_PATHS["ghost_images"]}{GHOST_IMAGES["dead"]}'), (45, 45))
    
    def get_targets(self):
        if self.player.x < 450:
            runaway_x = 900
        else:
            runaway_x = 0
        if self.player.y < 450:
            runaway_y = 900
        else:
            runaway_y = 0
        return_target = (380, 400)
        if self.powerup:
            if not self.blinky_dead and not self.eaten_ghost[0]:
                blink_target = (runaway_x, runaway_y)
            elif not self.blinky_dead and self.eaten_ghost[0]:
                if 340 < self.blinky_x < 560 and 340 < self.blinky_y < 500:
                    blink_target = (400, 100)
                else:
                    blink_target = (self.player.x, self.player.y)
            else:
                blink_target = return_target
            if not self.inky_dead and not self.eaten_ghost[1]:
                ink_target = (runaway_x, self.player.y)
            elif not self.inky_dead and self.eaten_ghost[1]:
                if 340 < self.inky_x < 560 and 340 < self.inky_y < 500:
                    ink_target = (400, 100)
                else:
                    ink_target = (self.player.x, self.player.y)
            else:
                ink_target = return_target
            if not self.pinky_dead:
                pink_target = (self.player.x, runaway_y)
            elif not self.pinky_dead and self.eaten_ghost[2]:
                if 340 < self.pinky_x < 560 and 340 < self.pinky_y < 500:
                    pink_target = (400, 100)
                else:
                    pink_target = (self.player.x, self.player.y)
            else:
                pink_target = return_target
            if not self.clyde_dead and not self.eaten_ghost[3]:
                clyd_target = (450, 450)
            elif not self.clyde_dead and self.eaten_ghost[3]:
                if 340 < self.clyde_x < 560 and 340 < self.clyde_y < 500:
                    clyd_target = (400, 100)
                else:
                    clyd_target = (self.player.x, self.player.y)
            else:
                clyd_target = return_target
        else:
            if not self.blinky_dead:
                if 340 < self.blinky_x < 560 and 340 < self.blinky_y < 500:
                    blink_target = (400, 100)
                else:
                    blink_target = (self.player.x, self.player.y)
            else:
                blink_target = return_target
            if not self.inky_dead:
                if 340 < self.inky_x < 560 and 340 < self.inky_y < 500:
                    ink_target = (400, 100)
                else:
                    ink_target = (self.player.x, self.player.y)
            else:
                ink_target = return_target
            if not self.pinky_dead:
                if 340 < self.pinky_x < 560 and 340 < self.pinky_y < 500:
                    pink_target = (400, 100)
                else:
                    pink_target = (self.player.x, self.player.y)
            else:
                pink_target = return_target
            if not self.clyde_dead:
                if 340 < self.clyde_x < 560 and 340 < self.clyde_y < 500:
                    clyd_target = (400, 100)
                else:
                    clyd_target = (self.player.x, self.player.y)
            else:
                clyd_target = return_target
        return [blink_target, ink_target, pink_target, clyd_target]
    
    def reset_positions(self):
        self.player.reset()
        self.blinky_x = BLINKY_START_X
        self.blinky_y = BLINKY_START_Y
        self.blinky_direction = BLINKY_START_DIRECTION
        self.inky_x = INKY_START_X
        self.inky_y = INKY_START_Y
        self.inky_direction = INKY_START_DIRECTION
        self.pinky_x = PINKY_START_X
        self.pinky_y = PINKY_START_Y
        self.pinky_direction = PINKY_START_DIRECTION
        self.clyde_x = CLYDE_START_X
        self.clyde_y = CLYDE_START_Y
        self.clyde_direction = CLYDE_START_DIRECTION
        self.eaten_ghost = [False, False, False, False]
        self.blinky_dead = False
        self.inky_dead = False
        self.clyde_dead = False
        self.pinky_dead = False
        self.direction_command = 0
        self.powerup = False
        self.power_counter = 0
        self.startup_counter = 0
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.direction_command = 0
                if event.key == pygame.K_LEFT:
                    self.direction_command = 1
                if event.key == pygame.K_UP:
                    self.direction_command = 2
                if event.key == pygame.K_DOWN:
                    self.direction_command = 3
                if event.key == pygame.K_SPACE and (self.game_over or self.game_won):
                    self.lives = LIVES_START
                    self.score = SCORE_START
                    self.board.reset()
                    self.game_over = False
                    self.game_won = False
                    self.reset_positions()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT and self.direction_command == 0:
                    self.direction_command = self.player.direction
                if event.key == pygame.K_LEFT and self.direction_command == 1:
                    self.direction_command = self.player.direction
                if event.key == pygame.K_UP and self.direction_command == 2:
                    self.direction_command = self.player.direction
                if event.key == pygame.K_DOWN and self.direction_command == 3:
                    self.direction_command = self.player.direction
        return True
    
    def update(self):
        if self.counter < 19:
            self.counter += 1
            if self.counter > 3:
                self.flicker = False
        else:
            self.counter = 0
            self.flicker = True
            
        if self.powerup and self.power_counter < POWERUP_DURATION:
            self.power_counter += 1
        elif self.powerup and self.power_counter >= POWERUP_DURATION:
            self.power_counter = 0
            self.powerup = False
            self.eaten_ghost = [False, False, False, False]
            
        if self.startup_counter < STARTUP_DURATION and not self.game_over and not self.game_won:
            self.moving = False
            self.startup_counter += 1
        else:
            self.moving = True

        self.screen.fill(SCREEN_COLOR)
        self.board.draw(self.screen, self.flicker)
        center_x, center_y = self.player.get_center()
        
        if self.powerup:
            self.ghost_speeds = GHOST_SPEEDS_POWERUP.copy()
        else:
            self.ghost_speeds = GHOST_SPEEDS.copy()
            
        if self.eaten_ghost[0]:
            self.ghost_speeds[0] = 2
        if self.eaten_ghost[1]:
            self.ghost_speeds[1] = 2
        if self.eaten_ghost[2]:
            self.ghost_speeds[2] = 2
        if self.eaten_ghost[3]:
            self.ghost_speeds[3] = 2
        if self.blinky_dead:
            self.ghost_speeds[0] = 4
        if self.inky_dead:
            self.ghost_speeds[1] = 4
        if self.pinky_dead:
            self.ghost_speeds[2] = 4
        if self.clyde_dead:
            self.ghost_speeds[3] = 4

        self.game_won = self.board.is_game_won()

        player_circle = pygame.draw.circle(self.screen, 'black', (center_x, center_y), 20, 2)
        self.player.draw(self.screen, self.flicker)
        
        self.targets = self.get_targets()
        
        blinky = Ghost(self.blinky_x, self.blinky_y, self.targets[0], self.ghost_speeds[0], self.blinky_img, self.blinky_direction, self.blinky_dead, self.blinky_box, 0, self.board.level, self.powerup, self.eaten_ghost, self.spooked_img, self.dead_img, self.screen)
        inky = Ghost(self.inky_x, self.inky_y, self.targets[1], self.ghost_speeds[1], self.inky_img, self.inky_direction, self.inky_dead, self.inky_box, 1, self.board.level, self.powerup, self.eaten_ghost, self.spooked_img, self.dead_img, self.screen)
        pinky = Ghost(self.pinky_x, self.pinky_y, self.targets[2], self.ghost_speeds[2], self.pinky_img, self.pinky_direction, self.pinky_dead, self.pinky_box, 2, self.board.level, self.powerup, self.eaten_ghost, self.spooked_img, self.dead_img, self.screen)
        clyde = Ghost(self.clyde_x, self.clyde_y, self.targets[3], self.ghost_speeds[3], self.clyde_img, self.clyde_direction, self.clyde_dead, self.clyde_box, 3, self.board.level, self.powerup, self.eaten_ghost, self.spooked_img, self.dead_img, self.screen)
        
        self.ui.draw_misc(self.screen, self.score, self.powerup, self.lives, self.game_over, self.game_won)

        turns_allowed = self.player.check_position(self.board.level)
        if self.moving:
            self.player.move(turns_allowed)
            if not self.blinky_dead and not blinky.in_box:
                self.blinky_x, self.blinky_y, self.blinky_direction = blinky.move_blinky()
            else:
                self.blinky_x, self.blinky_y, self.blinky_direction = blinky.move_clyde()
            if not self.pinky_dead and not pinky.in_box:
                self.pinky_x, self.pinky_y, self.pinky_direction = pinky.move_pinky()
            else:
                self.pinky_x, self.pinky_y, self.pinky_direction = pinky.move_clyde()
            if not self.inky_dead and not inky.in_box:
                self.inky_x, self.inky_y, self.inky_direction = inky.move_inky()
            else:
                self.inky_x, self.inky_y, self.inky_direction = inky.move_clyde()
            self.clyde_x, self.clyde_y, self.clyde_direction = clyde.move_clyde()
            
        score_increase, powerup_triggered, powerup_reset = self.board.check_collision(center_x, center_y)
        self.score += score_increase
        if powerup_triggered:
            self.powerup = True
            self.power_counter = 0
            self.eaten_ghost = [False, False, False, False]
            
        if not self.powerup:
            if (player_circle.colliderect(blinky.rect) and not blinky.dead) or \
                    (player_circle.colliderect(inky.rect) and not inky.dead) or \
                    (player_circle.colliderect(pinky.rect) and not pinky.dead) or \
                    (player_circle.colliderect(clyde.rect) and not clyde.dead):
                if self.lives > 0:
                    self.lives -= 1
                    self.startup_counter = 0
                    self.powerup = False
                    self.power_counter = 0
                    self.reset_positions()
                else:
                    self.game_over = True
                    self.moving = False
                    self.startup_counter = 0
                    
        if self.powerup and player_circle.colliderect(blinky.rect) and not blinky.dead and not self.eaten_ghost[0]:
            self.blinky_dead = True
            self.eaten_ghost[0] = True
            self.score += (2 ** self.eaten_ghost.count(True)) * 100
        if self.powerup and player_circle.colliderect(inky.rect) and not inky.dead and not self.eaten_ghost[1]:
            self.inky_dead = True
            self.eaten_ghost[1] = True
            self.score += (2 ** self.eaten_ghost.count(True)) * 100
        if self.powerup and player_circle.colliderect(pinky.rect) and not pinky.dead and not self.eaten_ghost[2]:
            self.pinky_dead = True
            self.eaten_ghost[2] = True
            self.score += (2 ** self.eaten_ghost.count(True)) * 100
        if self.powerup and player_circle.colliderect(clyde.rect) and not clyde.dead and not self.eaten_ghost[3]:
            self.clyde_dead = True
            self.eaten_ghost[3] = True
            self.score += (2 ** self.eaten_ghost.count(True)) * 100

        if self.direction_command == 0 and turns_allowed[0]:
            self.player.direction = 0
        if self.direction_command == 1 and turns_allowed[1]:
            self.player.direction = 1
        if self.direction_command == 2 and turns_allowed[2]:
            self.player.direction = 2
        if self.direction_command == 3 and turns_allowed[3]:
            self.player.direction = 3

        if blinky.in_box and self.blinky_dead:
            self.blinky_dead = False
        if inky.in_box and self.inky_dead:
            self.inky_dead = False
        if pinky.in_box and self.pinky_dead:
            self.pinky_dead = False
        if clyde.in_box and self.clyde_dead:
            self.clyde_dead = False

        pygame.display.flip()
        return True
    
    def run(self):
        run = True
        while run:
            self.timer.tick(FPS)
            run = self.handle_events()
            if run:
                run = self.update()
        pygame.quit()
