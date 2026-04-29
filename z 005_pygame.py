"""import pygame , sys
pygame.init()
sr = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit
            sys.exit"""


import pygame
pygame.init()
rn = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Welcome to pygame")

run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()


