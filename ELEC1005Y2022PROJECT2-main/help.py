# -*- coding: utf-8 -*-


import pygame

black = pygame.Color(0, 0, 0)
background = pygame.Color(169, 209, 142)

class Help:
    """
    Help page:
        explains keys can be used for the game
    """

    def __init__(self) -> None:
        self.finish = False

    def show(self):
        self.finish = False
    #All help guidelines written
    def display_help(self, screen):
        screen.fill(background)

        self.text_display(
            screen, "Keyboard control:", 10, 10, black)

        self.text_display(
            screen, "UP: snake move towards up", 10, 30, black)
        self.text_display(
            screen, "DOWN: snake move towards down", 10, 50, black)
        self.text_display(
            screen, "LEFT: snake move towards left", 10, 70, black)
        self.text_display(
            screen, "RIGHT: snake move towards right", 10, 90, black)

        self.text_display(
            screen, "SPACE: pause and resume", 10, 110, black)
        self.text_display(
            screen, "H: open the help instructions", 10, 130, black)
        self.text_display(
            screen, "Q: quit current game", 10, 150, black)
        self.text_display(
            screen, "ESCAPE: exit the game", 10, 170, black)
    #
    def text_display(self,  screen, message, x, y, color):
        font = pygame.font.SysFont(None, 25)
        text = font.render(message, True, color)
        screen.blit(text, (x, y))

    def is_finish(self):
        return self.finish

    #Quitting help page
    def close_page(self):
        self.finish = True
