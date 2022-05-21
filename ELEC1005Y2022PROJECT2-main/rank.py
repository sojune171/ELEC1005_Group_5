# -*- coding: utf-8 -*-

import pygame
import os
import json

background = pygame.Color(169, 209, 142)
class Rank:
    """
    Rank page:
        Show the top 10 records
    """



    def __init__(self) -> None:
        self.finish = False

    def show(self):

        self.finish = False
        if os.path.exists("Rank.json"):
            with open("Rank.json", "r", encoding="utf-8") as file:
                json_data = file.read()
                if len(json_data.strip()) > 0:
                    self.rank_list = json.loads(json_data)
                else:
                    self.rank_list = []
    #displaying ranks that was recieved
    def display_rank(self, screen, color):
        screen.fill(background)
        for i, val in enumerate(self.rank_list):
            self.message_display(screen, str(i+1)+" :  " +
                                 str(val), 10, 10+i*20,  color)
    #displaying message
    def message_display(self,  screen, message, x, y, color):
        font = pygame.font.SysFont(None, 25)
        text = font.render(message, True, color)
        screen.blit(text, (x, y))

    def is_finish(self):
        return self.finish
    #closing rank page
    def close_page(self):
        self.finish = True
