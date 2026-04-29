""" 
import pygame , sys
pygame.init()
sr = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit
            sys.exit

import pygame
pygame.init()
rn = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Welcome to pygame")
run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit() """

# ________________________________________________________________________
""" >> pygame ^ random >>> Running Program code
run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.circle(winds, BLUE, (20, 20), 20, 20)
    pygame.display.update() """
# ________________________________________________________________________



import pygame
import random
pygame.init()

# Create >>> Screen widndow :
WIDTH, HEIGHT = 800, 500
winds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Ball")

# Colors : (RED >> BLUE >> GREEN) >>>>>>>> RBG
WHITE = (255, 255, 255)
GREEN = (20, 250, 40)
RED = (250, 40, 20)
BLUE = (43, 150, 200)
PURPLE = (80, 54, 200)
BLACK = (0, 0, 0)

# Clock >>> setting time :
Clock = pygame.time.Clock()

# Setting Player :
Player_wid = 70
Player_hig = 15
x_play = WIDTH // 2 - Player_wid / 2
y_play = HEIGHT - 80
Play_spd = 5

# Score :
score_point = 0
font = pygame.font.SysFont("Forte", 25)

run = True  

while run :
    Clock.tick(50)
    winds.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # pygame.draw.circle(winds, RED, (25, 25), 20, 20)
    # pygame.display.update()
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] and x_play > 0 :
        x_play -= Play_spd

    if key[pygame.K_LEFT] and x_play < WIDTH - x_play:
        x_play += Play_spd

    # Draw score
    score_text = font.render(f"Player Score : {score_point}", True, BLACK)
    winds.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

pygame.quit()
        