import pygame
from pygame.draw import *
from random import randint
from random import choice
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 700))

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
class Ball:
    def __init__ (self):
            self.color = choice(COLORS)
            self.radius = randint(10, 100)
            self.coords = [randint(100, 1100), randint(100, 600)]
            self.speed = [randint(-10, 10), randint(-10, 10)]
    def paint(self):
            circle(screen, self.color, self.coords, self.radius) 
    def hit_target(self, hit_coords):
        if ((hit_coords[0]-self.coords[0])**2 + (hit_coords[1]-self.coords[1])**2
            <= self.radius**2):
            circle(screen, BLACK, self.coords, self.radius)
            self.color = choice(COLORS)
            self.radius = randint(10, 100)
            self.coords = [randint(100, 1100), randint(100, 600)]
            self.speed = [randint(-10, 10), randint(-10, 10)]
            self.paint()
            pygame.display.update()
            return(1)
        else:
            return(0)
    def move(self):
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
targets = [Ball() for i in range(15)]
for target in targets:
    target.paint()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
pygame.font.init()
k = 0
while not finished:
    rect(screen, BLACK, (1100, 0, 100, 100))
    labelFont = pygame.font.SysFont('Monaco', 100)
    surface_counter = labelFont.render(str(k), False, RED)
    screen.blit(surface_counter, (1100, 0))
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(BLACK)
    for target in targets:
        #circle(screen, BLACK, target.coords, target.radius)
        target.move()
        target.paint()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for target in targets:
                k += target.hit_target(event.pos)
pygame.quit()
