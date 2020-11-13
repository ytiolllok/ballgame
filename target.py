from random import choice
from random import randint
import pygame
from pygame.draw import *
from math import cos
from math import sqrt  
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
a = 0
b = 0
class anytarget(): 
    def __init__ (self, screen):
            self.color = choice(COLORS)
            self.radius = randint(10, 100)
            self.coords = [randint(100, 1100), randint(100, 600)]
            self.speed = [randint(-10, 10), randint(-10, 10)]
            self.screen = screen


class ball(anytarget):
    def paintcircle(self):
            circle(self.screen, self.color, self.coords, self.radius) 
    def hit_target(self, hit_coords):
        if ((hit_coords[0]-self.coords[0])**2 + (hit_coords[1]-self.coords[1])**2
            <= self.radius**2):
            circle(self.screen, BLACK, self.coords, self.radius)
            self.color = choice(COLORS)
            self.radius = randint(10, 100)
            self.coords = [randint(100, 1100), randint(100, 600)]
            self.speed = [randint(-10, 10), randint(-10, 10)]
            self.paintcircle()
            pygame.display.update()
            return(1)
        else:
            return(0)
    def movecircle(self):
        if (0 < self.coords[0] + self.speed[0] < 1200):
            a = 1
        else:
            a = -1
        if (0 < self.coords[1] + self.speed[1] < 600):
            b = 1
        else:
            b = -1
        self.speed = [a*self.speed[0], b*self.speed[1]]
        self.coords = [self.coords[0] + self.speed[0],
        self.coords[1] + self.speed[1]]

    
class shrek(anytarget):
    def paintshrek(self):
        size = 150
        screen = self.screen
        self.coords[0] = int(self.coords[0])
        self.coords[1] = int(self.coords[1])
        ellipse(screen, (255, 255, 255), (self.coords[0], self.coords[1], size, int(0.3 * size)))
        ellipse(screen, (255, 255, 255), (self.coords[0], int(self.coords[1]+ 0.2 * size), int(0.1 * size), int(0.5 * size)))
        ellipse(screen, (255, 255, 255), (int(self.coords[0] + 0.2*size), int(self.coords[1]+ 0.15 * size), int(0.1 * size), int(0.5 * size)))
        ellipse(screen, (255, 255, 255), (int(self.coords[0] + 0.7*size), int(self.coords[1]+ 0.1 * size), int(0.1 * size), int(0.5 * size)))
        ellipse(screen, (255, 255, 255), (int(self.coords[0] + 0.85*size), int(self.coords[1]+ 0.2 * size), int(0.1 * size), int(0.5 * size)))
        ellipse(screen, (255, 255, 255), (int(self.coords[0] + 0.85*size), int(self.coords[1] - 0.3 * size), int(0.2 * size), int(0.5 * size)))
        ellipse(screen, (255, 255, 255), (int(self.coords[0] + 0.85*size), int(self.coords[1] - 0.4 * size), int(0.4 * size), int(0.2 * size)))
        ellipse(screen, (201, 120, 245), (int(self.coords[0] + 0.95*size), int(self.coords[1] - 0.38 * size), int(0.1 * size), int(0.1 * size)))
        ellipse(screen, (1, 2, 5), (int(self.coords[0] + 0.97*size), int(self.coords[1] - 0.35 * size), int(0.05 * size), int(0.05 * size)))
        ellipse(screen, (255, 255, 255), (int(self.coords[0] + 0.97*size), int(self.coords[1] - 0.37 * size), int(0.05 * size), int(0.05 * size)))
        circle(screen, (255, 255, 255), (self.coords[0], int(self.coords[1]+ 0.7 * size)), int(0.07 * size))
        circle(screen, (255, 255, 255), (int(self.coords[0] + 0.2*size), int(self.coords[1]+ 0.65 * size)), int(0.07 * size))
        circle(screen, (255, 255, 255), (int(self.coords[0] + 0.7*size), int(self.coords[1]+ 0.6 * size)), int(0.07 * size))
        circle(screen, (255, 255, 255), (int(self.coords[0] + 0.85*size), int(self.coords[1]+ 0.7 * size)), int(0.07 * size))
    def hit_shrek(self, hitcoords):
        if (self.screen.get_at(hitcoords) == (255, 255, 255, 255)) or  (self.screen.get_at(hitcoords) == (201, 120, 245, 255)) or (self.screen.get_at(hitcoords) == (1, 2, 5, 255)):
            self.coords = [randint(100, 1100), randint(100, 600)]
            return(5)
        else:
            return(0)
    def move_shrek(self):
        if (0 < self.coords[0] + self.speed[0] < 1200):
            a = 1
        else:
            a = -1
        if (0 < self.coords[1] + self.speed[1] < 600):
            b = 1
        else:
            b = -1
        self.speed = [a*self.speed[0], b*self.speed[1]]
        self.coords = [self.coords[0] + self.speed[0],
        (self.coords[0]*(0.6-0.2*sqrt((cos(self.coords[0])**2))))]
    
