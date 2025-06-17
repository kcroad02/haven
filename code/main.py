import pygame
import os
import time
from os.path import join
from random import randint, uniform
from save import *




class Game():
    def __init__(self, level):
        self.level = level
        self.data = ["Press Space to begin!"]
        self.animated_text = display_text(self.data, 75)
       
    def play(self):
        if self.level == 0:
            self.data = ['Haven Town','A ROGBONE creation','Press space to continue']
            self.level += 1
        elif self.level == 1:
            self.data = ["test."]
            self.level += 1
        else:
            self.data = ['you','the save-data corrupted im sorry gamer','Press space to reset save data . . .']
            self.level = 0
        self.animated_text = display_text(self.data, 75)
        

    def update(self):
        self.animated_text.update()
        if self.animated_text.isAllDone() == True:
            self.save()
            self.play()

    def save(self):
        output_file_path = os.path.join('code', 'save.py')
        with open(output_file_path, 'w') as f:
            f.write("level = " + str(self.level))
            f.close()

class display_text():
        def __init__(self, stringList, speed):
            # speed is how quick the text goes, it's inputted in the class object, not the class
            self.speed = speed
            # counter is for individually parsing each character
            self.counter = 0
            # active text is for the active string in the list
            self.active_text = 0
            # stringList is the string list
            self.stringList = stringList
            # done is if a string is done and can move onto the next string in the list
            self.done = False
            # all of the strings in the stringList are done
            self.allDone = False

        def update(self):

            # just_keys is on released, get_pressed is every time it's pressed
            just_keys = pygame.key.get_just_pressed()
            keys = pygame.key.get_pressed()

            # if space & message is done+list not over, next text in the stringList, done is false, and counter is 0
            if just_keys[pygame.K_SPACE]:
                if self.done and self.active_text < (len(self.stringList)-1):
                    self.active_text += 1
                    self.message = self.stringList[self.active_text]
                    self.done = False
                    self.counter = 0
                if self.done and self.active_text == (len(self.stringList)-1):
                    self.allDone = True
                    return self.allDone
            # increases the speed by using counter varaible
            if keys[pygame.K_RETURN]:
                self.counter += 10
            
            # self.message is the specific string in the stringList
            self.message = self.stringList[self.active_text]
            if self.counter < self.speed * len(self.message):
                self.counter += 1
            elif self.counter >= self.speed * len(self.message):
                self.done = True
                
            # renders it based off the individual parsed characters based on a speed, True (idk), and the color in rgb
            self.text_surf = font.render(str(self.message[0:self.counter//(self.speed)]), True, (240,240,240), wraplength=800)
            #rectangle for around the text
            self.text_rect = self.text_surf.get_frect(topleft = (WINDOW_WIDTH-(WINDOW_WIDTH-20), WINDOW_HEIGHT-(WINDOW_HEIGHT-20)))
            # blit is b-something l-something image transfer
            global display_surface
            display_surface.blit(self.text_surf, self.text_rect)
        def isAllDone(self):
            return self.allDone

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Haven Town')
running = True
clock = pygame.time.Clock()
gameLevel = Game(level)

# imports
font = pygame.font.Font(join('images', 'Oxanium-Bold.ttf'),40)

if __name__ == '__main__':
    while running:
        # Deltatime
        dt = clock.tick() / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        display_surface.fill("#080a08")
        gameLevel.update()
        pygame.display.update()
pygame.quit()