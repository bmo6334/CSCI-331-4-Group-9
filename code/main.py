import pygame

pygame.font.init()
screen = pygame.display.set_mode((497,600))

pygame.display.set_caption("Sudoku Solver")
cell_size = 500 // 9
x=0
y=0
dif = 500 / 9
value = 0

# store base grid for resets
base_grid =[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
grid = [row[:] for row in base_grid]

font1 = pygame.font.SysFont('Arial', 38)
font2 = pygame.font.SysFont('Arial', 20)

# draw selected box to edit
def draw_selection_box():
    left = x * cell_size
    top = y * cell_size
    right = left + cell_size
    bottom = top + cell_size

    if left < 0: left = 0
    if top < 0: top = 0
    if right > 500: right = 500
    if bottom > 500: bottom = 500

    pygame.draw.rect(screen, (255, 0, 255), (left, top, right - left, bottom - top), 5)

# helper function
def get_cord(pos):
    global x, y
    x = int(pos[0] // cell_size)
    y = int(pos[1] // cell_size)
    x = max(0, min(8, x))
    y = max(0, min(8, y))

# to draw the entire board
def draw():
    board_size = cell_size * 9
    for row in range(9):
        for col in range(9):
            num = grid[row][col]
            if base_grid[row][col] != 0:
                color = (190, 190, 190) # grey for base_grid
            elif num != 0:
                color = (100, 190, 255) # light blue for inputs
            else:
                color = (255, 255, 255) # white for empty

            pygame.draw.rect(
                screen,
                color,
                (col * cell_size, row * cell_size, cell_size, cell_size)
            )
            if num != 0:
                text_color = (0, 0, 0)
                text_surf = font1.render(str(num), True, text_color)
                text_rect = text_surf.get_rect(center=(
                    col * cell_size + cell_size // 2,
                    row * cell_size + cell_size // 2
                ))
                screen.blit(text_surf, text_rect)

    # grid lines
    for i in range(10):
        thick = 7 if i % 3 == 0 else 2
        pos = i * cell_size
        pygame.draw.line(screen, (0, 0, 0), (0, pos), (board_size, pos), thick)
        pygame.draw.line(screen, (0, 0, 0), (pos, 0), (pos, board_size), thick)


# text instructions
def info_display():
    text1 = font2.render("Press R to Reset the board", 1, (0, 0, 0))
    text2 = font2.render("TODO: Add button to start Backtracking", 1, (0, 0, 0))
    text3 = font2.render("TODO: Add button to start CSP Backtracking", 1, (0, 0, 0))
    screen.blit(text1, (5, 500))
    screen.blit(text2, (5, 520))
    screen.blit(text3, (5, 540))

# to keep the window from closing
run = True
flag1 = 0
flag2 = 0
while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
        if event.type == pygame.KEYDOWN:
            # input number in empty space/replace a space
            if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4,
                             pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:
                if base_grid[y][x] == 0:
                    val = int(event.unicode)
                    grid[y][x] = val
            # delete space
            if event.key in [pygame.K_BACKSPACE, pygame.K_DELETE]:
                if base_grid[y][x] == 0:
                    grid[y][x] = 0
            # reset to original board
            if event.key == pygame.K_r:
                flag2 = 0
                grid = [row[:] for row in base_grid]
    draw()
    if flag1 == 1:
        draw_selection_box()
    info_display()
    pygame.display.update()
pygame.quit()