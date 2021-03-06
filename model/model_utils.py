"""
    This module defines some utility functions and the resources image for chessboard printing
    * from_matrix_to_chessboard: convert from matrix format to chessboard format
    * from_chessboard_to_matrix: convert from chessboard format to matrix format
    * getInitialConfiguration: define the initial configuration of pieces on the chessboard
"""

import numpy as np

from PIL import Image
from enum import Enum
from chess_enum import Piece

w_pawn = Image.open("./resources/gui/whitePawn.png")
w_rook = Image.open("./resources/gui/whiteRook.png")
w_knight = Image.open("./resources/gui/whiteKnight.png")
w_bishop = Image.open("./resources/gui/whiteBishop.png")
w_queen = Image.open("./resources/gui/whiteQueen.png")
w_king = Image.open("./resources/gui/whiteKing.png")
b_pawn = Image.open("./resources/gui/blackPawn.png")
b_rook = Image.open("./resources/gui/blackRook.png")
b_knight = Image.open("./resources/gui/blackKnight.png")
b_bishop = Image.open("./resources/gui/blackBishop.png")
b_queen = Image.open("./resources/gui/blackQueen.png")
b_king = Image.open("./resources/gui/blackKing.png")
board = Image.open("./resources/gui/board.png")

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

conversions = {0 : "a",
                1 : "b",
                2 : "c",
                3 : "d",
                4 : "e",
                5 : "f",
                6 : "g",
                7 : "h"}

def from_matrix_to_chessboard(m_index):
    return str(conversions[m_index[0]]) + str(m_index[1] + 1)

def from_chessboard_to_matrix(c_index):
    keys_list = list(conversions.keys())
    values_list = list(conversions.values())

    row_index = keys_list[values_list.index(c_index[0])]
    col_index = int(c_index[1]) - 1
    return (row_index, col_index)

def getInitialConfiguration():
    configuration = np.full((8,8), Piece.EMPTY)

    ## WHITE PIECES
    configuration[0,0] = Piece.W_ROOK;      configuration[1,0] = Piece.W_PAWN
    configuration[0,1] = Piece.W_KNIGHT;    configuration[1,1] = Piece.W_PAWN
    configuration[0,2] = Piece.W_BISHOP;    configuration[1,2] = Piece.W_PAWN
    configuration[0,3] = Piece.W_QUEEN;     configuration[1,3] = Piece.W_PAWN
    configuration[0,4] = Piece.W_KING;      configuration[1,4] = Piece.W_PAWN
    configuration[0,5] = Piece.W_BISHOP;    configuration[1,5] = Piece.W_PAWN
    configuration[0,6] = Piece.W_KNIGHT;    configuration[1,6] = Piece.W_PAWN
    configuration[0,7] = Piece.W_ROOK;      configuration[1,7] = Piece.W_PAWN

    ## BLACK PIECES
    configuration[7,0] = Piece.B_ROOK;      configuration[6,0] = Piece.B_PAWN
    configuration[7,1] = Piece.B_KNIGHT;    configuration[6,1] = Piece.B_PAWN
    configuration[7,2] = Piece.B_BISHOP;    configuration[6,2] = Piece.B_PAWN
    configuration[7,3] = Piece.B_QUEEN;     configuration[6,3] = Piece.B_PAWN
    configuration[7,4] = Piece.B_KING;      configuration[6,4] = Piece.B_PAWN
    configuration[7,5] = Piece.B_BISHOP;    configuration[6,5] = Piece.B_PAWN
    configuration[7,6] = Piece.B_KNIGHT;    configuration[6,6] = Piece.B_PAWN
    configuration[7,7] = Piece.B_ROOK;      configuration[6,7] = Piece.B_PAWN

    return configuration.T
