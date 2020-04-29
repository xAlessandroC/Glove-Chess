import pygame
from pygame.locals import *
import numpy as np
import sys
sys.path.append('./model/')

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (70,40)

from chessboard import *
from executer import *

width = 250
height = 250
model = None

mode = "debug"

## LOAD PIECES
board = pygame.image.load("./resources/gui/board.png")
board = pygame.transform.scale(board, (width, height))

pieces_group = pygame.sprite.Group()
w_pawn = pygame.sprite.Sprite(pieces_group);    w_pawn.image = pygame.transform.scale(pygame.image.load("./resources/gui/whitePawn.png"),(int(width/8), int(height/8)))
w_rook = pygame.sprite.Sprite(pieces_group);    w_rook.image = pygame.transform.scale(pygame.image.load("./resources/gui/whiteRook.png"),(int(width/8), int(height/8)))
w_knight = pygame.sprite.Sprite(pieces_group);  w_knight.image = pygame.transform.scale(pygame.image.load("./resources/gui/whiteKnight.png"),(int(width/8), int(height/8)))
w_bishop = pygame.sprite.Sprite(pieces_group);  w_bishop.image = pygame.transform.scale(pygame.image.load("./resources/gui/whiteBishop.png"),(int(width/8), int(height/8)))
w_queen = pygame.sprite.Sprite(pieces_group);   w_queen.image = pygame.transform.scale(pygame.image.load("./resources/gui/whiteQueen.png"),(int(width/8), int(height/8)))
w_king = pygame.sprite.Sprite(pieces_group);    w_king.image = pygame.transform.scale(pygame.image.load("./resources/gui/whiteKing.png"),(int(width/8), int(height/8)))

b_pawn = pygame.sprite.Sprite(pieces_group);    b_pawn.image = pygame.transform.scale(pygame.image.load("./resources/gui/blackPawn.png"),(int(width/8), int(height/8)))
b_rook = pygame.sprite.Sprite(pieces_group);    b_rook.image = pygame.transform.scale(pygame.image.load("./resources/gui/blackRook.png"),(int(width/8), int(height/8)))
b_knight = pygame.sprite.Sprite(pieces_group);  b_knight.image = pygame.transform.scale(pygame.image.load("./resources/gui/blackKnight.png"),(int(width/8), int(height/8)))
b_bishop = pygame.sprite.Sprite(pieces_group);  b_bishop.image = pygame.transform.scale(pygame.image.load("./resources/gui/blackBishop.png"),(int(width/8), int(height/8)))
b_queen = pygame.sprite.Sprite(pieces_group);   b_queen.image = pygame.transform.scale(pygame.image.load("./resources/gui/blackQueen.png"),(int(width/8), int(height/8)))
b_king = pygame.sprite.Sprite(pieces_group);    b_king.image = pygame.transform.scale(pygame.image.load("./resources/gui/blackKing.png"),(int(width/8), int(height/8)))

pieces = [w_pawn,w_rook,w_knight,w_bishop,w_queen,w_king,
          b_pawn,b_rook,b_knight,b_bishop,b_queen,b_king]

PIECES = {
"w_pawn": w_pawn,
"w_rook": w_rook,
"w_knight": w_knight,
"w_bishop": w_bishop,
"w_queen": w_queen,
"w_king": w_king,
"b_pawn": b_pawn,
"b_rook": b_rook,
"b_knight": b_knight,
"b_bishop": b_bishop,
"b_queen": b_queen,
"b_king": b_king,
}


centers = []
start = (int(width*0.008),int(height*0.008))
length = 31
count = 0
for i in range(8):
    for j in range(8):
        centers.append((start[0]+i*length,start[1]+j*length))
        count = count + 1

centers = np.array(centers).reshape((8,8,2))

# centers = np.flip(centers, 1)
chessboard = Chessboard.getInstance()

## FUNCTIONS
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def clickedCell(mouse_pos):
    i = int(mouse_pos[0]/31)
    j = int(mouse_pos[1]/31)

    return i,j

def detectCollidedSprite(mouse_pos):
    global model
    print(PIECES)
    i,j = clickedCell(mouse_pos)

    print(i,j)
    if i>=0 and i<=7 and j>=0 and j<=7:
        print("NAME:",model[i,j].name.lower())
        try:

            return PIECES[model[i,j].name.lower()].image, i, j
        except:
            return None, -1, -1

    return None, -1, -1

def startGui():
    global model, board

    pygame.init()
    size = (width, height)
    screen = pygame.display.set_mode(size)
    icon = pygame.image.load("./resources/gui/chess.png")
    pygame.display.set_caption("AR Chess")
    pygame.display.set_icon(icon)

    ## BACKGROUND
    background = board
    circle = pygame.image.load("./resources/gui/circle.png")
    circle = pygame.transform.scale(circle,(10,10))

    ## DRAWINGS SETTINGS
    font_title = pygame.font.SysFont('Comic Sans MS', 44)
    font_mode = pygame.font.SysFont('Comic Sans MS', 20)


    carryOn = True
    clock = pygame.time.Clock()
    pressed = False
    pressed_sprite = None
    cell_x = -1
    cell_y = -1

    while carryOn:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(background,(0,0))
        model = chessboard.getPieces()
        # model = np.flip(model,1)

        for i in range(8):
            for j in range(8):
                if model[i,j] != Piece.EMPTY:
                    if i != cell_x or j != cell_y:
                        screen.blit(PIECES[model[i,j].name.lower()].image,centers[i,j])

        if pressed and pressed_sprite != None:
            screen.blit(pressed_sprite,(mouse_pos[0]-15,mouse_pos[1]-15))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                carryOn = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    carryOn = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pressed = True
                pressed_sprite, cell_x, cell_y = detectCollidedSprite(mouse_pos)
                print("DETECTED: ", pressed_sprite, cell_x, cell_y)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                ##chessboard update
                if pressed_sprite != None:
                    i,j = clickedCell(mouse_pos)

                    from_ = str(conversions[cell_x]) + str(cell_y + 1)
                    to_ = str(conversions[i]) + str(j + 1)
                    # print(from_, to_)
                    if mode == "debug":
                        try:
                            checkAndExecuteMove(from_,to_)
                        except Exception as e:
                            print(e)
                            pass
                    if mode == "update":
                        chessboard.update(from_, to_)


                    pressed = False
                    pressed_sprite = None
                    cell_x = -1
                    cell_y = -1

        pygame.display.flip()
        clock.tick(60)


    pygame.quit()

if __name__ == "__main__":
    startGui()
