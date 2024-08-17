import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Tic Tac Toe")


# Draw grid lines
line1 = pygame.Rect((0, 200, 800, 5))
line2 = pygame.Rect((0, 400, 800, 5))
line3 = pygame.Rect((200, 0, 5, 800))
line4 = pygame.Rect((400, 0, 5, 800))


# Board to keep track of the game state
score = [[0 for _ in range(3)] for _ in range(3)]


# Draw cross and circle
def draw_cross(x, y):
    pygame.draw.line(screen, (0, 0, 255), (x - 50, y - 50), (x + 50, y + 50), 5)
    pygame.draw.line(screen, (0, 0, 255), (x - 50, y + 50), (x + 50, y - 50), 5)


def draw_circle(x, y):
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 50, 5)


# Function to check for a winner
def check_winner(score):
    for row in score:
        if row[0] == row[1] == row[2] != 0:
            return row[0]

    for col in range(3):
        if score[0][col] == score[1][col] == score[2][col] != 0:
            return score[0][col]

    if score[0][0] == score[1][1] == score[2][2] != 0:
        return score[0][0]

    if score[0][2] == score[1][1] == score[2][0] != 0:
        return score[0][2]

    return 0


# Function to display game over message
def game_over(winner):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 64)
    if winner == 1:
        text = font.render("Player One Wins!", True, (0, 255, 0))
    elif winner == 2:
        text = font.render("Player Two Wins!", True, (0, 255, 0))
    else:
        text = font.render("It's a Draw!", True, (0, 255, 0))

    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()
    quit()


run = True
moves = 0
x_turn = True


while run:

    # Clear the screen before drawing
    screen.fill((0, 0, 0))

    # Draw grid
    pygame.draw.rect(screen, (255, 255, 255), line1)
    pygame.draw.rect(screen, (255, 255, 255), line2)
    pygame.draw.rect(screen, (255, 255, 255), line3)
    pygame.draw.rect(screen, (255, 255, 255), line4)

    # Redraw all existing marks
    for i in range(3):
        for j in range(3):
            if score[i][j] == 1:
                draw_cross(j * 200 + 100, i * 200 + 100)
            elif score[i][j] == 2:
                draw_circle(j * 200 + 100, i * 200 + 100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // 200
            col = x // 200

            if score[row][col] == 0:
                if x_turn:
                    draw_cross(col * 200 + 100, row * 200 + 100)
                    score[row][col] = 1
                else:
                    draw_circle(col * 200 + 100, row * 200 + 100)
                    score[row][col] = 2

                x_turn = not x_turn
                moves += 1

                winner = check_winner(score)
                if winner or moves == 9:
                    game_over(winner)

    pygame.display.update()

pygame.quit()
