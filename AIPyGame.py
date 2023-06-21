import pygame

# 초기화
pygame.init()

# 게임 화면 크기 설정
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("플랫포머 게임")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# 플레이어 클래스 정의
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = screen_height - 100
        self.vel_y = 0
        self.jump_power = -10

    def update(self):
        # 플레이어 이동
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # 중력 적용
        self.vel_y += 0.5
        self.rect.y += self.vel_y

        # 화면 경계 검사
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width

        # 플랫폼과의 충돌 처리
        if self.rect.y >= screen_height - self.rect.height:
            self.rect.y = screen_height - self.rect.height
            self.vel_y = 0

        # 점프 처리
        if keys[pygame.K_SPACE] and self.rect.y == screen_height - self.rect.height:
            self.vel_y = self.jump_power

# 플랫폼 클래스 정의
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

# 플레이어 생성
player = Player()
all_sprites.add(player)

# 플랫폼 생성
platform = Platform(0, screen_height - 50, screen_width, 50)
all_sprites.add(platform)
platforms.add(platform)

# 게임 루프
running = True
clock = pygame.time.Clock()
while running:
    # 프레임 설정
    clock.tick(30)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 업데이트
    all_sprites.update()

    # 충돌 검사
    hits = pygame.sprite.spritecollide(player, platforms, False)
    if hits:
        player.vel_y = 0
        player.rect.y = hits[0].rect.y - player.rect.height

    # 화면 그리기
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

# 게임 종료
pygame.quit()
