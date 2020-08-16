import pygame
from sudoku import Board
pygame.init()

WHITE = (255, 255, 255)
BLUE = (53, 92, 226)
RED = (255, 0, 0)
WIDTH = 800
HEIGHT = 600
SQ_SIZE = 50
B_START_HEIGHT = 105

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0, 0, 0))

title_font = pygame.font.Font("resources/8-bit Madness.ttf", 50)
text_font = pygame.font.Font("resources/8-bit Madness.ttf", 25)
number_font = pygame.font.Font("resources/Roboto-Thin.ttf", 20)

def draw_screen(board, surface, valid):
    draw_text(surface)
    draw_numbers(board, surface, valid)
    for i in range(1, 11):
        if i%3 == 1:
            pygame.draw.line(surface, WHITE, (i*SQ_SIZE, B_START_HEIGHT), (i*SQ_SIZE, B_START_HEIGHT+(9*SQ_SIZE)), 3)
            pygame.draw.line(surface, WHITE, (SQ_SIZE, B_START_HEIGHT+((i-1)*SQ_SIZE)), (10*SQ_SIZE, B_START_HEIGHT+((i-1)*SQ_SIZE)), 3)
        else:
            pygame.draw.line(surface, WHITE, (i*SQ_SIZE, B_START_HEIGHT), (i*SQ_SIZE, B_START_HEIGHT+(9*SQ_SIZE)))
            pygame.draw.line(surface, WHITE, (SQ_SIZE, B_START_HEIGHT+((i-1)*SQ_SIZE)), (10*SQ_SIZE, B_START_HEIGHT+((i-1)*SQ_SIZE)))

def draw_text(surface):
    title = title_font.render("Sudoku", True, WHITE)
    title_rect = title.get_rect(center=(int(WIDTH/2), int(SQ_SIZE/2)))
    surface.blit(title, title_rect)
    pygame.draw.line(surface, WHITE, (SQ_SIZE, SQ_SIZE), (WIDTH-SQ_SIZE, SQ_SIZE), 4)

    #side text for instructions
    text_list = [
        "KEYS",
        "\'G\' to generate new board",
        "\'R\' to reset board",
        "\'S\' to solve board",
        "SPACE to check board",
        "\'Q\' to quit" 
    ]
    end_sq = SQ_SIZE*10
    x = end_sq + int((WIDTH - end_sq)/2)
    for i in range(6):
        y = (B_START_HEIGHT+SQ_SIZE)+(i*SQ_SIZE)+(int(SQ_SIZE/2))
        text = text_font.render(text_list[i], True, WHITE)
        text_rect = text.get_rect(center=(x, y))
        surface.blit(text, text_rect)
    pygame.draw.line(surface, WHITE, (end_sq+SQ_SIZE, B_START_HEIGHT+2*SQ_SIZE), (WIDTH-SQ_SIZE, B_START_HEIGHT+2*SQ_SIZE))

def draw_numbers(grid, surface, valid):
    for i in range(grid.rows):
        for j in range(grid.columns):
            if grid.board[i][j] != 0:
                x = (j+1)*SQ_SIZE+(int(SQ_SIZE/2))
                y = (i*SQ_SIZE)+B_START_HEIGHT+(int(SQ_SIZE/2))
                if valid:
                    if grid.board[i][j] != grid.ans_board[i][j]:
                        num = number_font.render(str(grid.board[i][j]), True, RED)
                        num_rect = num.get_rect(center=(x, y))
                        surface.blit(num, num_rect)
                    else:
                        num = number_font.render(str(grid.board[i][j]), True, WHITE)
                        num_rect = num.get_rect(center=(x, y))
                        surface.blit(num, num_rect)

                else:
                    num = number_font.render(str(grid.board[i][j]), True, WHITE)
                    num_rect = num.get_rect(center=(x, y))
                    surface.blit(num, num_rect)

def highlighted_box(coords):
    x = coords[0]//SQ_SIZE
    y = (coords[1]-B_START_HEIGHT)//SQ_SIZE
    return (x*SQ_SIZE, (y*SQ_SIZE)+B_START_HEIGHT, SQ_SIZE, SQ_SIZE)

def enter_val(grid, value, coords):
    row = (coords[1]-B_START_HEIGHT)//SQ_SIZE
    col = (coords[0]//SQ_SIZE)-1
    grid.set_val(row, col, value)

def del_entry(grid, coords):
    row = (coords[1]-B_START_HEIGHT)//SQ_SIZE
    col = (coords[0]//SQ_SIZE)-1
    grid.set_zero(row, col)

def main():
    b = Board()
    b.generate_board()
    selected = [-1, -1]

    pygame.display.update()
    running = True
    validating = False

    while running:
        screen.fill((0, 0, 0))
        draw_screen(b, screen, validating)
        if selected != [-1, -1] and SQ_SIZE < selected[0] < 10*SQ_SIZE and B_START_HEIGHT < selected[1] < B_START_HEIGHT+(10*SQ_SIZE):
            pygame.draw.rect(screen, BLUE, highlighted_box(selected), 3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                validating = False
                selected[0] = event.pos[0]
                selected[1] = event.pos[1]
            if event.type == pygame.KEYDOWN:
                validating = False
                if event.key == pygame.K_BACKSPACE:
                    del_entry(b, selected)
                if event.key == pygame.K_1:
                    enter_val(b, 1, selected)
                if event.key == pygame.K_2:
                    enter_val(b, 2, selected)
                if event.key == pygame.K_3:
                    enter_val(b, 3, selected)
                if event.key == pygame.K_4:
                    enter_val(b, 4, selected)
                if event.key == pygame.K_5:
                    enter_val(b, 5, selected)
                if event.key == pygame.K_6:
                    enter_val(b, 6, selected)
                if event.key == pygame.K_7:
                    enter_val(b, 7, selected)
                if event.key == pygame.K_8:
                    enter_val(b, 8, selected)
                if event.key == pygame.K_9:
                    enter_val(b, 9, selected)
                if event.key == pygame.K_g:
                    b.generate_new()
                if event.key == pygame.K_r:
                    b.reset_board()
                if event.key == pygame.K_SPACE:
                    validating = True
                if event.key == pygame.K_s:
                    b.solve()
                if event.key == pygame.K_q:
                    pygame.quit()
        pygame.display.update()

if __name__ == "__main__":
    main()
