import pygame

pygame.init()

size = [1600, 900]
ssmiddlesize = [128, 76]
mmmiddlesize = [55, 210]

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

ss = pygame.image.load("C:\Python\PyGame\SpaceShip.png").convert_alpha()
ss = pygame.transform.scale(ss, (ssmiddlesize[0], ssmiddlesize[1]))

mm = pygame.image.load("C:\Python\PyGame\Missile.png").convert_alpha()
mm = pygame.transform.scale(mm, (mmmiddlesize[0], mmmiddlesize[1]))

sms_x = round(ssmiddlesize[0]/2)
sms_y = round(ssmiddlesize[1]/2)

mms_x = round(mmmiddlesize[0]/2)
mms_y = round(mmmiddlesize[1]/2)

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
    screen.blit(ss, (x_pos-sms_x, y_pos-sms_y))
    screen.blit(mm, (x_pos-mms_x, y_pos-mms_y))

    pygame.draw.circle(screen, (204, 102, 255), (x_pos-50, y_pos), 5)
    pygame.draw.circle(screen, (204, 102, 255), (x_pos+50, y_pos), 5)            
    pygame.display.update()

pygame.quit()