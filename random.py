import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))

screen.fill((0,0,0))

pygame.draw.line(screen,pygame.color.THECOLORS['white'],(500,450),(400,300))
pygame.draw.circle(screen,pygame.color.THECOLORS['white'],(300,300),50)
pygame.draw.rect(screen,pygame.color.THECOLORS['white'],(200,100,50,100))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
