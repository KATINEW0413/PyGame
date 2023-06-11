import pygame

pygame.init()

size = [1600, 900]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyGame made by MJ")

fps = pygame.time.Clock()

x_pos = screen.get_size()[0]/2
y_pos = screen.get_size()[1]/2

up_go = False
down_go = False
right_go = False
left_go = False

ssmiddlesize1 = 128
ssmiddlesize2 = 67

ss = pygame.image.load("C:\Python\PyGame\SpaceShip.png").convert_alpha()
ss = pygame.transform.scale(ss, (ssmiddlesize1, ssmiddlesize2))

sms_x = round(ssmiddlesize1/2)
sms_y = round(ssmiddlesize2/2)

to_x = 0
to_y = 0

move = 4

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_go = False
            if event.key == pygame.K_DOWN:
                down_go = False
            if event.key == pygame.K_RIGHT:
                right_go = False
            if event.key == pygame.K_LEFT:
                left_go = False

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
    screen.blit(ss, (x_pos-sms_x, y_pos-sms_y))
    pygame.draw.circle(screen, (204, 102, 255), (x_pos, y_pos), 15)            
    pygame.display.update()

pygame.quit()