# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:22:20 2018

@author: zou
"""

import pygame
import time
from pygame.locals import KEYDOWN, K_RIGHT, K_LEFT, K_UP, K_DOWN, K_ESCAPE
from pygame.locals import QUIT

from game import Game

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(108, 122, 137)
bright_grey = pygame.Color(210, 215, 211)
#modified
background = pygame.Color(169, 209, 142)
grid = pygame.Color(112,173,71)

green = pygame.Color(0, 200, 0)
bright_green = pygame.Color(0, 255, 0)
red = pygame.Color(200, 0, 0)
bright_red = pygame.Color(255, 0, 0)
blue = pygame.Color(32, 178, 170)
bright_blue = pygame.Color(32, 200, 200)
yellow = pygame.Color(255, 205, 0)
bright_yellow = pygame.Color(255, 255, 0)

game = Game()
rect_len = game.settings.rect_len
snake = game.snake
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((game.settings.width * 15, game.settings.height * 15))
pygame.display.set_caption('Gluttonous')

crash_sound = pygame.mixer.Sound('./sound/crash.wav')
background_music = pygame.mixer.Sound('./sound/BossTheme.wav')


def text_objects(text, font, color=black):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def message_display(text, x, y, color=black):
    large_text = pygame.font.SysFont('comicsansms', 50)
    text_surf, text_rect = text_objects(text, large_text, color)
    text_rect.center = (x, y)
    screen.blit(text_surf, text_rect)


def message_display_small(text, x, y, color=black):
    small = pygame.font.SysFont('comicsansms', 10)
    text_surf, text_rect = text_objects(text, small, color)
    text_rect.center = (x, y)
    screen.blit(text_surf, text_rect)


def button(msg, x, y, w, h, inactive_color, active_color, action=None, parameter=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if parameter != None:
                action(parameter)
            else:
                action()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))

    smallText = pygame.font.SysFont('comicsansms', 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = (x + (w / 2), y + (h / 2))
    screen.blit(TextSurf, TextRect)


pygame.mixer.music.load('./sound/BossTheme.wav')
pygame.mixer.music.play(-1)




def on_off():
    music_playing = pygame.mixer.music.get_busy()
    if music_playing:
        pygame.mixer.music.fadeout(1000)
        return
    pygame.mixer.music.play()

def quitgame():
    pygame.quit()
    quit()


def crash():
    pygame.mixer.Sound.play(crash_sound)
    message_display('crashed', game.settings.width / 2 * 15, game.settings.height / 3 * 15, white)
    time.sleep(2)

def initial_interface():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        screen.fill(background)
        message_display('Gluttonous', game.settings.width / 2 * 15, game.settings.height / 8 * 15)
        button('Go!', 250, 180, 100, 60, green, bright_green, game_loop, 'human')
        button('Quit', 250, 290, 100, 60, red, bright_red, quitgame)
        button('Music', 20, 360, 60, 40, grey, bright_grey, on_off)
        message_display_small('On/Off', game.settings.width / 1 * 1.7, game.settings.height / 1 * 14.5)

        snake_image = pygame.image.load('images/snake.png')
        snake_image = pygame.transform.scale(snake_image, (240, 200))
        screen.blit(snake_image, (-20, 130))


        pygame.display.update()
        pygame.time.Clock().tick(15)



def drawGrid():
    blockSize = 15
    for x in range(0, 410, blockSize):
        for y in range(0, 410, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, grid, rect, 1)

def game_loop(player, fps=10):
    game.restart_game()

    while not game.game_end():

        pygame.event.pump()

        move = human_move()
        fps = 5

        game.do_move(move)

        screen.fill(background)
        drawGrid()
        button('Music', 20, 360, 60, 40, grey, bright_grey, on_off)
        game.snake.blit(rect_len, screen)
        game.strawberry.blit(screen)
        game.blit_score(white, screen)

        pygame.display.flip()

        fpsClock.tick(fps)



    crash()


def human_move():
    direction = snake.facing

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                direction = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                direction = 'left'
            if event.key == K_UP or event.key == ord('w'):
                direction = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                direction = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    move = game.direction_to_int(direction)
    return move


if __name__ == "__main__":
    initial_interface()
