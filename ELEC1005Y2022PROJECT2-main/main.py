# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:22:20 2018

@author: zou
"""

import time

import pygame
from pygame.locals import (K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_SPACE, K_UP,
                           KEYDOWN, QUIT)

from game import Game
from help import Help
from rank import Rank

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

#modifed/added colours
grey = pygame.Color(108, 122, 137)
bright_grey = pygame.Color(210, 215, 211)
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


pygame.init()
# page initialize
game = Game()
help = Help()
rank = Rank()

rect_len = game.settings.rect_len
snake = game.snake
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode(
    (game.settings.width * 15, game.settings.height * 15))
pygame.display.set_caption('Gluttonous')

crash_sound = pygame.mixer.Sound('./sound/crash.wav')

#Background Music Version2
background_music = pygame.mixer.Sound('./sound/Happy Accident Advanced Loop With Intro.wav')


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

#playing background music in a loop
pygame.mixer.music.load('./sound/Happy Accident Advanced Loop With Intro.wav')
pygame.mixer.music.play(-1)

#Function which starts the music
def get_music_playing():
    return pygame.mixer.music.get_busy()

#Function to stop and resume music
def on_off():
    music_playing = pygame.mixer.music.get_busy()
    if music_playing:
        pygame.mixer.music.fadeout(350)
        return
    pygame.mixer.music.play()

def quitgame():
    pygame.quit()
    quit()


def crash():
    pygame.mixer.Sound.play(crash_sound)
    message_display('crashed', game.settings.width / 2 * 15,
                    game.settings.height / 3 * 15, white)
    
    # Display the current ranking, -1 means close the whole game
    if game.rank != -1:
        message_display('Ranking is:'+str(game.rank+1), game.settings.width / 2 * 15,
                        game.settings.height / 3 * 20, white)
    time.sleep(3)


def initial_interface():
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        #Background Colour changed to Green
        screen.fill(background)
        #Moved the Title Game Name Higher
        message_display('Gluttonous', game.settings.width / 2 * 15, game.settings.height / 8 * 15)

        #All buttons in Home Screen, all in one area on right down corner
        #Starting to play the game
        button('Go!', 220, 240, 80, 40, green, bright_green, game_loop, 'human')
        #Button to quit the game
        button('Quit', 320, 240, 80, 40, red, bright_red, quitgame)
        # add button for the help page
        button('Help', 220, 340, 80, 40, blue, bright_blue, help_loop)
        # add button for the rank page
        button('Rank', 320, 340, 80, 40, yellow, bright_yellow, rank_loop)
        #MUSIC on and off button on left down corner with the message of on and off
        button("Music: ON" if get_music_playing() else "Music: OFF", 20, 360, 120, 40, grey, bright_grey, on_off)
        message_display_small('On/Off', game.settings.width / 1 * 1.7, game.settings.height / 1 * 14.5)

        #Snake Image for the home screen
        snake_image = pygame.image.load('images/snake.png')
        snake_image = pygame.transform.scale(snake_image, (240, 200))
        screen.blit(snake_image, (-20, 130))

        pygame.display.update()
        pygame.time.Clock().tick(15)

#Function to draw grid on the game screen
def drawGrid():
    blockSize = 15
    for x in range(0, 410, blockSize):
        for y in range(0, 410, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, grid, rect, 1)

def help_loop(): 
    """
    Dealing with the interface of the help page
    """
    help.show()
    pygame.display.set_caption('Help')
    while not help.is_finish():
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            quitgame()

        screen.fill(white)

        help.display_help(screen)
        button('Close', 320, 0, 80, 40, red, bright_red, help.close_page)

        pygame.display.flip()
    pygame.display.set_caption('Gluttonous')


def rank_loop():
    """
    Dealing with the interface of the rank page
    """

    rank.show()
    pygame.display.set_caption('Rank')
    while not rank.is_finish():
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            quitgame()

        screen.fill(white)

        rank.display_rank(screen, black)
        button('Close', 320, 0, 80, 40, red, bright_red, rank.close_page)

        pygame.display.flip()
    pygame.display.set_caption('Gluttonous')


def game_loop(player, fps=10):
    game.restart_game()

    while not game.game_end():

        pygame.event.pump()

        move = human_move()
        fps = 5

        game.do_move(move)
        #filling screen background to green
        screen.fill(background)
        #Using drawGrid() to draw grids
        drawGrid()
        # add button to turn music on and off
        button("Music: ON" if get_music_playing() else "Music: OFF", 315, 0, 105, 30, grey, bright_grey, on_off)

        game.snake.blit(rect_len, screen)
        game.strawberry.blit(screen)
        game.blit_score(white, screen)

        # add button for pause and resume 
        button(game.pause and 'Resume' or 'Pause', 75, 0,
               105, 30, blue, bright_blue, game.pause_continue)
        # add button for quit the current game
        button('Quit', 195, 0,
               105, 30, red, bright_red, game.quit_game)

        pygame.display.flip()

        fpsClock.tick(fps)

    # skip the crash process if quit manually
    if not game.is_quit_current_game():
        crash()


def human_move():
    direction = snake.facing

    for event in pygame.event.get():
        if event.type == QUIT:
            quitgame()

        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == ord('d'):
                direction = 'right'
            if event.key == K_LEFT or event.key == ord('a'):
                direction = 'left'
            if event.key == K_UP or event.key == ord('w'):
                direction = 'up'
            if event.key == K_DOWN or event.key == ord('s'):
                direction = 'down'
            # 'Q' for quit current game
            if event.key == ord('q'):
                game.quit_game()
            # 'H' for get help instructions
            if event.key == ord('h'):
                help_loop()
            # 'SPACE' for pause and resume game
            if event.key == K_SPACE:
                game.pause_continue()
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    move = game.direction_to_int(direction)
    return move


if __name__ == "__main__":
    initial_interface()
