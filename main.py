import pygame

# ゲームの初期化
pygame.init()

# 画面サイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DotCraft")

# 色の定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 画面を白で塗りつぶす
    screen.fill(WHITE)

    # 画面の更新
    pygame.display.flip()

pygame.quit()