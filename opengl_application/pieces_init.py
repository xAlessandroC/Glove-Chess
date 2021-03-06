"""
    This module implements the functions for initializing chess pieces in the system and on the
    chessboard.
"""

import os
import glut_application as glta

from objloader_complete import *
from chessboard_model import *
from opengl_utils import *

## PIECES
PIECES_CONV = {
    "W_KING" : "Re_Bianco",
    "W_QUEEN" : "Regina_Bianca",
    "W_ROOK" : "Torre_Bianca",
    "W_BISHOP" : "Alfiere_Bianco",
    "W_KNIGHT" : "Cavallo_Bianco",
    "W_PAWN" : "Pedone_Bianco",
    "B_KING" : "Re_Nero",
    "B_QUEEN" : "Regina_Nera",
    "B_ROOK" : "Torre_Nera",
    "B_BISHOP" : "Alfiere_Nero",
    "B_KNIGHT" : "Cavallo_Nero",
    "B_PAWN" : "Pedone_Nero",
}

PIECES_DICT = {}
PIECES_POSITION = {}

id_chessboardList = None
id_selectionSprite = None


def load_pieces():
    directory = r"resources\chess_models_reduced"

    print("Loading pieces...")
    for piece in os.listdir(directory):
        piece_dir = directory + "\\" + piece
        for file in os.listdir(piece_dir):
            if file.startswith(piece) and file.endswith(".obj"):
                print("Loading "+piece+"...")
                complete_path = (os.path.join(piece_dir, file)).replace("\\","/")
                print(complete_path)
                obj = OBJ(complete_path)

                PIECES_DICT[piece] = obj

    PIECES_DICT["Puntatore"] = OBJ("resources/chess_models_reduced/Selection/selector.obj")
    print(PIECES_DICT)


def init_piece(centers):
    global id_selectionSprite, id_chessboardList

    _chessboard = Chessboard.getInstance()
    pieces = _chessboard.getPieces()

    # Loading chess pieces
    for i in range(8):
        for j in range(8):
            if pieces[i,j] != Piece.EMPTY:
                id = glGenLists(1)
                PIECES_POSITION[str(i)+"-"+str(j)] = id
                obj = PIECES_DICT[PIECES_CONV[pieces[i,j].name]]
                new_vertices = translateVertices(obj, *tuple(centers[i,j]), z=2)
                overwriteList(id, obj, new_vertices)

    # Loading chessboard
    id_chessboardList = glGenLists(1)
    obj = PIECES_DICT["Scacchiera"]
    overwriteList(id_chessboardList, obj, obj.vertices)

    # Loading selector
    id_selectionSprite = glGenLists(1)
    glta.obj_s = PIECES_DICT["Puntatore"]
    new_vertices = translateVertices(glta.obj_s, *tuple(centers[0,0]), z=13)
    overwriteList(id_selectionSprite, glta.obj_s, new_vertices)
