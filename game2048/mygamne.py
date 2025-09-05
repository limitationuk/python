BOARD_WIDTH = 800
BOARD_HEIGHT = 800
NUM_GRID = 4
GRID_SIZE = BOARD_WIDTH // NUM_GRID
BG_COLOR = (187, 173, 160)
TILE_MARGIN = 3
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

DEFAULT_COLOR = TILE_COLORS[0]

def draw_cell(screen, row, column, value):
    rect = pygame.Rect(column * GRID_SIZE+TILE_MARGIN, row * GRID_SIZE +
                       TILE_MARGIN, GRID_SIZE-TILE_MARGIN*2, GRID_SIZE-TILE_MARGIN*2)
    color = TILE_COLORS.get(value, DEFAULT_COLOR) #value가 없으면 기본 컬러 적용
    pygame.draw.rect(screen, color , rect)


def render_board(screen, board_map):
    screen.fill(BG_COLOR)

    for row in range(NUM_GRID):
        for column in range(NUM_GRID):
            draw_cell(screen, row, column, board_map[row][column])


if __name__ == "__main__":

    # Example file showing a basic pygame "game loop"
    import pygame

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((BOARD_HEIGHT, BOARD_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    board_map = [[0 for _ in range(NUM_GRID)] for _ in range(NUM_GRID)]

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        board_map[0][0] = 2
                        pass
                    case pygame.K_RIGHT:
                        board_map[0][1] = 4
                        pass
                    case pygame.K_UP:
                        board_map[0][2] = 8
                        pass
                    case pygame.K_DOWN:
                        board_map[0][3] = 16
                        pass
                    case _:
                        pass
                
        # fill the screen with a color to wipe away anything from last frame
        # screen.fill(BG_COLOR)

        # RENDER YOUR GAME HERE
        render_board(screen, board_map)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
