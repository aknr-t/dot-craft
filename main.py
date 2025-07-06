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
LIGHT_GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

# ブロックサイズ
BLOCK_SIZE = 20

# グリッドのサイズ
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# ワールドデータ (0: 空, 1: ブロック)
world = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 画面を白で塗りつぶす
    screen.fill(WHITE)

    # グリッドの描画
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, LIGHT_GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, LIGHT_GRAY, (0, y), (SCREEN_WIDTH, y))

    # ブロックの描画
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if world[y][x] == 1:
                pygame.draw.rect(screen, GREEN, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # 画面の更新
    pygame.display.flip()

pygame.quit()