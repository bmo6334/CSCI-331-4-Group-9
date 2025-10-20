import pygame

pygame.font.init()
screen = pygame.display.set_mode((500, 600))

pygame.display.set_caption("Sudoku Solver")

x=0
y=0
dif = screen.get_rect().x / 9
value = 0
grid =[
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

font1 = pygame.font.SysFont('Arial', 40)
font2 = pygame.font.SysFont('Arial', 20)

def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)

def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif

def draw():
    for i in grid:
        for j in i:
            if j != 0:
                pygame.draw.rect(screen, j, (dif, dif, dif))
                text1 = font1.render(str(j), True, (0, 0, 0))
                screen.blit(text1, (i * dif + 15, j * dif + 15))

    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick= 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)


# to keep the window from closing
run = True
flag1 = 0
flag2 = 0
while run:
    screen.fill((255, 255, 255))
    draw()
    draw_box()