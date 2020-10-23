import pygame
from pygame.draw import *
from target import ball, shrek
pygame.init()
RED = (255, 0, 0)
BLACK = (0, 0, 0)
FPS = 30
screen = pygame.display.set_mode((1200, 700))
targetcircles = [ball(screen) for i in range(15)]
for target in targetcircles:
    target.paintcircle()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
pygame.font.init()
k = 0
lama = shrek(screen)
pygame.init()
life = 1
time = 0
while not finished:
    labelFont = pygame.font.SysFont('Monaco', 100)
    surface_counter = labelFont.render(str(k), False, RED)
    screen.blit(surface_counter, (1100, 0))
    pygame.display.update()
    clock.tick(FPS)
    screen.fill(BLACK)
    lama.paintshrek()
    for target in targetcircles:
        target.movecircle()
        target.paintcircle()
    lama.move_shrek()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (life == 1):
                k += lama.hit_shrek(event.pos)
                for target in targetcircles:
                    k += target.hit_target(event.pos)
    time = pygame.time.get_ticks() 
    if (time > 30000):
        life = 0
        #print('caught', k, 'maslin')
        secondfont = pygame.font.SysFont('arial',100)
        score = secondfont.render((str(k)+' МАСЛИН ПОЙМАНО'), False, RED)
        screen.blit(score, (150, 350))    
    else:
        time_remain = labelFont.render(str('Осталось ' + str(30-int(time/1000))+ ' с'), False, RED)
        screen.blit(time_remain, (100, 0)) 
pygame.quit()
