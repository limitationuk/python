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

def rotate(is_cw, board_map):
    new_map = None
    if is_cw:
        #CW
        new_map = [list(row) for row in zip(*board_map[::-1])] #튜플은 수정불가 -> 리스트로 반환
    else:
        #ccw
        new_map = [list(row) for row in zip(*board_map)][::-1]
    return new_map

def merge_row(row):
    new_row = []
    skip_merge = False

    for i in range(NUM_GRID):
        if skip_merge is True:
            skip_merge = False
            continue
        if row[i] == 0: #값이 0이라면 그대로 진행
            continue
        elif i+1 < len(row) and row[i] == row[i+1]: # 마지막인덱스가 아니고, 현재 값이 다음 값과 같다면 값의 2배
            new_row.append(row[i]*2)
            skip_merge = True
        elif i < len(row):  # 마지막 인덱스가 아니라면
            new_row.append(row[i])
    while len(new_row) < NUM_GRID: # 길이나 4 이하면 0을 채워준다.
        new_row.append(0)
    return new_row

def push_and_merge(rotate_times, board_map):
    rotated_map = board_map
    
    #Rotate CW90 * rotate_times
    for _ in range(rotate_times):
        rotated_map = rotate(True,rotated_map)
    
    #Merge row
    new_board = []  #rotated_map도 가능?
    for row in rotated_map: 
        new_row = merge_row(row)
        new_board.append(new_row)

    #Rotate CCW90 * rotate_times
    for _ in range(rotate_times):
        new_board = rotate(False,new_board)

    return new_board

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
                rotate_times = -1
                match event.key:    
                    case pygame.K_LEFT:
                        rotate_times = 0
                    case pygame.K_RIGHT:
                        rotate_times = 2
                    case pygame.K_UP:
                        rotate_times = 3
                    case pygame.K_DOWN:
                        rotate_times = 1
                    case _:
                        pass
                if rotate_times != -1:
                    push_and_merge(rotate_times,board_map)
                
        # fill the screen with a color to wipe away anything from last frame
        # screen.fill(BG_COLOR)

        # RENDER YOUR GAME HERE
        render_board(screen, board_map)

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()
