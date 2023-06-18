import pygame
import random

pygame.init()

size = [1600, 900]
Spaceshipmiddlesize = [128, 76]
Missilemiddlesize = [140, 37]
kirbysize = [110, 96]
ghostsize = [121, 121]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyGame made by MJ")

fps = pygame.time.Clock()

x_pos = screen.get_size()[0]/2
y_pos = screen.get_size()[1]/2

up_go = False
down_go = False
right_go = False
left_go = False
space_go = False

Spaceship = pygame.image.load("C:\Python\PyGame\SpaceShip.png").convert_alpha()
Spaceship = pygame.transform.scale(Spaceship, (Spaceshipmiddlesize[0], Spaceshipmiddlesize[1]))

Missile = pygame.image.load("C:\Python\PyGame\Missile.png").convert_alpha()
Missile = pygame.transform.scale(Missile, (Missilemiddlesize[0], Missilemiddlesize[1]))

Kirby = pygame.image.load("C:\Python\PyGame\Kirby.png").convert_alpha()
Kirby = pygame.transform.scale(Kirby, (kirbysize[0], kirbysize[1]))

Ghost = pygame.image.load("C:\Python\PyGame\Ghost.png").convert_alpha()
Ghost = pygame.transform.scale(Ghost, (ghostsize[0], ghostsize[1]))

sms_x = round(Spaceshipmiddlesize[0]/2)
sms_y = round(Spaceshipmiddlesize[1]/2)

mms_x = round(Missilemiddlesize[0]/2)
mms_y = round(Missilemiddlesize[1]/2)

kirby_x = round(kirbysize[0]/2)
kirby_y = round(kirbysize[1]/2)

ghost_x = round(ghostsize[0]/2)
ghost_y = round(ghostsize[1]/2)

move = 6

play = True

while play:
    deltaTime = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_go = True
            if event.key == pygame.K_DOWN:
                down_go = True
            if event.key == pygame.K_RIGHT:
                right_go = True
            if event.key == pygame.K_LEFT:
                left_go = True
            if event.key == pygame.K_SPACE:
                space_go = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_go = False
            if event.key == pygame.K_DOWN:
                down_go = False
            if event.key == pygame.K_RIGHT:
                right_go = False
            if event.key == pygame.K_LEFT:
                left_go = False
            if event.key == pygame.K_SPACE:
                space_go = False
    if up_go == True:
        y_pos -= move
        if y_pos <= 0:
            y_pos = 0
    if down_go == True:
        y_pos += move
        if y_pos >= 900:
            y_pos = 900
    if right_go == True:
        x_pos += move
        if x_pos >= 1600:
            x_pos = 1600
    if left_go == True:
        x_pos -= move
        if x_pos <= 0:
            x_pos = 0

    screen.fill((0, 0, 0))
    screen.blit(Spaceship, (x_pos-sms_x, y_pos-sms_y))
    screen.blit(Missile, (x_pos-mms_x, y_pos-mms_y))
    screen.blit(Kirby, (x_pos-kirby_x, y_pos-kirby_y))
    screen.blit(Ghost, (x_pos-ghost_x, y_pos-ghost_y))

    pygame.display.update()

pygame.quit()