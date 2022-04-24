import pygame
from sys import exit

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# pozivanje pygame
pygame.init()

# prozor
surface = pygame.display.set_mode((400, 400))
TILE_WIDTH = 100
offset = (400 - (TILE_WIDTH * 3)) / 2


# naslov prozora
pygame.display.set_caption("TicTacToe")

surface.fill(WHITE)

font = pygame.font.SysFont("monospace", 60)
small_font = pygame.font.SysFont("monospace", 30)

PLAYER_ONE_SYMBOL = 1
PLAYER_TWO_SYMBOL = 2


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = 0

    def __str__(self):
        return str(self.symbol)

    def __repr__(self):
        return str(self.symbol) + str([str(self.x), str(self.y)])

    def mark(self, symbol):
        # mark the tile with the correct symbol for the player
        # after this we check for win conditions
        self.symbol = symbol

    def draw(self, surface):
        rectangle = pygame.Rect(self.x, self.y, TILE_WIDTH, TILE_WIDTH)
        # draw the rectangle. Have to draw 2 rects to get a stroke :(
        pygame.draw.rect(surface, BLACK, rectangle, 1)
        if self.symbol == PLAYER_ONE_SYMBOL:
            text = "X"
        elif self.symbol == PLAYER_TWO_SYMBOL:
            text = "O"
        else:
            text = " "

        label = font.render(text, 1, BLACK)
        text_x = self.x - (label.get_rect().width / 2) + (TILE_WIDTH / 2)
        text_y = self.y - (label.get_rect().height / 2) + (TILE_WIDTH / 2)
        surface.blit(font.render(text, 1, BLACK), (text_x, text_y))


def check_horizontal_row(board, row_num):
    item = []
    for tile in board[row_num]:
        item.append(tile.symbol)

    # we can use python count to check the amount of items of a certain value
    if item.count(PLAYER_ONE_SYMBOL) == len(item):
        return PLAYER_ONE_SYMBOL
    elif item.count(PLAYER_TWO_SYMBOL) == len(item):
        return PLAYER_TWO_SYMBOL
    else:
        return 0


def check_vertical_row(board, col_num):
    item = []
    for row in board:
        item.append(row[col_num].symbol)
    # we can use python count to check the amount of items of a certain value
    if item.count(PLAYER_ONE_SYMBOL) == len(item):
        return PLAYER_ONE_SYMBOL
    elif item.count(PLAYER_TWO_SYMBOL) == len(item):
        return PLAYER_TWO_SYMBOL
    else:
        return 0


def check_diagonal_row(board):
    # only 2 diagonal lines. Build 2 lists
    item1 = [board[0][0].symbol, board[1][1].symbol, board[2][2].symbol]
    item2 = [board[0][2].symbol, board[1][1].symbol, board[2][0].symbol]

    if item1.count(PLAYER_ONE_SYMBOL) == len(item1):
        return PLAYER_ONE_SYMBOL
    elif item1.count(PLAYER_TWO_SYMBOL) == len(item1):
        return PLAYER_TWO_SYMBOL

    if item2.count(PLAYER_ONE_SYMBOL) == len(item2):
        return PLAYER_ONE_SYMBOL
    elif item2.count(PLAYER_TWO_SYMBOL) == len(item2):
        return PLAYER_TWO_SYMBOL

    return 0


def get_winner(board):
    for i in range(len(game_board)):
        player = check_horizontal_row(game_board, i)
        if player > 0:
            return player

    for j in range(len(game_board[i])):
        player = check_vertical_row(game_board, j)
        if player > 0:
            return player

    return check_diagonal_row(game_board)


def board_filled(board):
    """
    Checks if the board is all filled
    :param board:
    :return:
    """
    for row in board:
        for tile in row:
            if tile.symbol == 0:
                return False
    return True


def build_board():
    board = []
    for i in range(0, 3):
        row = []
        for j in range(0, 3):
            tile_x = (j * TILE_WIDTH) + offset
            tile_y = (i * TILE_WIDTH) + offset
            row.append(Tile(tile_x, tile_y))
        board.append(row)
    return board


game_board = build_board()

current_player = PLAYER_ONE_SYMBOL
game_over = False
winner = None

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # mark the appropriate tile
            # get the position of the mouse
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # check each tile to see if it's in that tile
            for row in game_board:
                for tile in row:
                    if mouse_x >= tile.x and mouse_x <= tile.x + TILE_WIDTH:
                        if mouse_y >= tile.y and mouse_y <= tile.y + TILE_WIDTH:
                            # its in this tile, so we can mark it with the current player's symbol
                            tile.mark(current_player)
                            # go to the next player
                            if current_player == PLAYER_ONE_SYMBOL:
                                current_player = PLAYER_TWO_SYMBOL
                            else:
                                current_player = PLAYER_ONE_SYMBOL

    # draw all the tiles
    # we need to clear the screen first. In this case we want to update the entire screen
    if game_over:
        # render the game over screen
        surface.fill(WHITE)
        label = small_font.render("Game Over", 1, BLACK)
        text_y = label.get_rect().height
        surface.blit(label, (0, 0))
        if winner is None:
            label = small_font.render("It's a draw!", 1, BLACK)
        else:
            label = small_font.render("Player " + str(winner) + " wins!", 1, BLACK)
        surface.blit(label, (0, text_y))
    else:
        surface.fill(WHITE)
        for row in game_board:
            for tile in row:
                tile.draw(surface)

        # check for win conditions
        player = get_winner(game_board)

        if player > 0:
            game_over = True
            winner = player
        elif board_filled(game_board):
            game_over = True

    pygame.display.update()
