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
BLUE = (0, 0, 255)

# ブロックサイズ
BLOCK_SIZE = 20

# グリッドのサイズ
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# ワールドデータ (0: 空, 1: ブロック)
world = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# 初期ブロックの配置 (テスト用)
world[GRID_HEIGHT // 2][GRID_WIDTH // 2] = 1
world[GRID_HEIGHT // 2][GRID_WIDTH // 2 + 1] = 1
world[GRID_HEIGHT // 2 + 1][GRID_WIDTH // 2] = 1
world[GRID_HEIGHT // 2 + 1][GRID_WIDTH // 2 + 1] = 1

# プレイヤーの初期位置
player_x = GRID_WIDTH // 2
player_y = GRID_HEIGHT // 2

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= 1
            if event.key == pygame.K_RIGHT:
                player_x += 1
            if event.key == pygame.K_UP:
                player_y -= 1
            if event.key == pygame.K_DOWN:
                player_y += 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            grid_x = mouse_x // BLOCK_SIZE
            grid_y = mouse_y // BLOCK_SIZE

            # グリッドの範囲内かチェック
            if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                if event.button == 1:  # 左クリックでブロックを配置
                    world[grid_y][grid_x] = 1
                elif event.button == 3:  # 右クリックでブロックを破壊
                    world[grid_y][grid_x] = 0

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

    # プレイヤーの描画
    pygame.draw.rect(screen, BLUE, (player_x * BLOCK_SIZE, player_y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    # 画面の更新
    pygame.display.flip()

pygame.quit()