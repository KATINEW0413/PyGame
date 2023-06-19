import pygame
import random

pygame.init()

size = [650, 900]
screen = pygame.display.set_mode(size)

kirby_transform = random.randint(96, 554)


title = "PyGame made by MJ"
pygame.display.set_caption(title)

clock = pygame.time.Clock()
color = (0, 0, 0)

Spaceshipmiddlesize = [128, 76]
Missilemiddlesize = [37, 140]
kirbysize = [110, 96]
ghostsize = [121, 121]

x_pos = screen.get_size()[0]/2
y_pos = screen.get_size()[1]/2

up_go = False
down_go = False
right_go = False
left_go = False
space_go = False

ss = pygame.image.load("C:\Python\PyGame\SpaceShip.png").convert_alpha()
ss = pygame.transform.scale(ss, (Spaceshipmiddlesize[0], Spaceshipmiddlesize[1]))
ss_sx, ss_sy = ss.get_size()
ss_x = round((size[0]/2)-(ss_sx/2))
ss_y = round(size[1]-ss_sy-25)

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
kirbymove = 2
kirbyDownmove = 110
play = True
live = True

mmmm = mms_y + size[1]/2

# copy Kirby
kirby_time = 0
kirbies = []
random_time = random.randrange(100, 200)


# Shooting Missile
shootMS = []

while play:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right_go = True
            if event.key == pygame.K_LEFT:
                left_go = True
            if event.key == pygame.K_SPACE:
                x_pos_missile = x_pos + mms_x/2
                shootMS.append([x_pos_missile, mmmm])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_go = False
            if event.key == pygame.K_LEFT:
                left_go = False
    if right_go == True:
        x_pos += move
        if x_pos >= 517:
            x_pos = 517
    if left_go == True:
        x_pos -= move
        if x_pos <= 5:
            x_pos = 5




    if live == True:
        kirbyDownmove += 2

    screen.fill(color)
    screen.blit(ss, (x_pos, ss_y))
    #screen.blit(Missile, (x_pos-mms_x, y_pos-mms_y))
    screen.blit(Kirby, (kirby_transform, kirbyDownmove))
    #screen.blit(Ghost, (x_pos-ghost_x, y_pos-ghost_y))
    # 커비 여러마리 생성

    pygame.display.update()

pygame.quit()