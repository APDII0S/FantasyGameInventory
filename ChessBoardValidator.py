# Chess board validator
# Ace - 2025-03-26

# This program will look at a chess board, and based on these rules...:
    # A valid board will only have one white king and one black king
    # Each player can't have a piece count exceeding 16
        # Each player's pawn count can't exceed 8
    # All pieces must be on a valid space from '1a' to '8h'

# ...it will verify the legitimacy of the chess board

# Piece names will begin either either of the two prefixes: 'w' or 'b' to represent piece color



"""""Valid chess board sample data"""""

# Standard starting position

sample_1 = {
    "a8": "brook", "b8": "bknight", "c8": "bbishop", "d8": "bqueen", "e8": "bking",
    "f8": "bbishop", "g8": "bknight", "h8": "brook",
    "a7": "bpawn", "b7": "bpawn", "c7": "bpawn", "d7": "bpawn",
    "e7": "bpawn", "f7": "bpawn", "g7": "bpawn", "h7": "bpawn",
    "a2": "wpawn", "b2": "wpawn", "c2": "wpawn", "d2": "wpawn",
    "e2": "wpawn", "f2": "wpawn", "g2": "wpawn", "h2": "wpawn",
    "a1": "wrook", "b1": "wknight", "c1": "wbishop", "d1": "wqueen", "e1": "wking",
    "f1": "wbishop", "g1": "wknight", "h1": "wrook"
}

# Plausible mid-game position

sample_2 = {
    "a8": "brook", "c8": "bbishop", "e8": "bking", "g8": "bknight", "h8": "brook",
    "a7": "bpawn", "b7": "bpawn", "d7": "bpawn", "e7": "bpawn", "f7": "bpawn", "h7": "bpawn",
    "a6": "wpawn",
    "b4": "wknight", "c4": "wpawn",
    "d2": "wpawn", "e2": "wpawn", "f2": "wpawn", "g2": "wpawn", "h2": "wpawn",
    "a1": "wrook", "c1": "wbishop", "e1": "wking", "g1": "wknight", "h1": "wrook"
}

# Endgame position

sample_3 = {
    "a8": "bpawn",  
    "h1": "wpawn",
    "e8": "bking", "e1": "wking"
}


"""""Invalid sample data"""

# Too many kings

sample_4 = {
    "e8": "bking", "e1": "wking",
    "d8": "bking",  # Extra black king
    "d1": "wking",  # Extra white king
    "a1": "wrook", "h1": "wrook",
    "a8": "brook", "h8": "brook"
}


# Too many pieces on one side

sample_5 = {
    "a8": "brook", "b8": "bknight", "c8": "bbishop", "d8": "bqueen", "e8": "bking",
    "f8": "bbishop", "g8": "bknight", "h8": "brook",
    "a7": "bpawn", "b7": "bpawn", "c7": "bpawn", "d7": "bpawn",
    "e7": "bpawn", "f7": "bpawn", "g7": "bpawn", "h7": "bpawn",
    "a6": "bqueen",  # Extra black queen (17 pieces for black)
    "a1": "wrook", "b1": "wknight", "c1": "wbishop", "d1": "wqueen", "e1": "wking",
    "f1": "wbishop", "g1": "wknight", "h1": "wrook",
    "a2": "wpawn", "b2": "wpawn", "c2": "wpawn", "d2": "wpawn",
    "e2": "wpawn", "f2": "wpawn", "g2": "wpawn", "h2": "wpawn"
}


"""~ Renamed from `boardValidation` to `isValidChessBoard` ~"""

def isValidChessBoard(board):

    # Are king counts valid?

    wkings = 0
    bkings = 0

    # for v in board.values():
    #    if v == 'wking':
    #        wkings += 1
    #    elif v == 'bking':
    #        bkings += 1

    for v in board.values():
        if v == 'wking':
            wkings += 1
        elif v == 'bking':
            bkings += 1

            

    """~ No need for the constant validation messages. It's just messy otherwise. ~"""

    #   "if wkings == 1 and bkings == 1:
    #       print("Kings are good so far...")
    #
    #   else:
    #       return False"



    """~ More efficient execution below. ~"""

    if wkings != 1 or bkings != 1:
        return "Invalid king count"
    
    
    # No one player has a piece count exceeding 16?

    wpieces = 0
    bpieces = 0

    for v in board.values():
        if v[0] == 'w':
            wpieces += 1
        elif v[0] == 'b':
            bpieces += 1



    """~ No need for the constant validation messages. It's just messy otherwise. ~"""

    #   """if wpieces <= 16:
    #       print("White pieces are good.")
    #
    #   else:
    #       return False
    #
    #   if bpieces <= 16:
    #       print("Black pieces are alright.")
    #
    #   else:
    #       return False"""
    

    """~ More efficient execution below. ~"""

    if wpieces > 16 or bpieces > 16:
        return "Too many pieces."



    # Are each player's pawn counts valid?

    wpawns = 0
    bpawns = 0

    for v in board.values():
        if v == 'wpawn':
            wpawns += 1
        elif v == 'bpawn':
            bpawns += 1



    """~ No need for the constant validation messages. It's just messy otherwise. ~"""

    #    """if wpawns <= 8:
    #        print("White's pawns are fine.")
    #
    #    else:
    #        return False
    #    
    #    if bpawns <= 8:
    #        print("Black's pieces are fine.")
    #
    #    else:
    #        return False"""


    """~ More efficient execution below. ~"""
    
    if wpawns > 8 or bpawns > 8:
        return "Too many pawns."



    """~ Inefficient logic. ~"""

    # Are pieces on valid spaces?

    #   """alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #
    #   for k in board.keys():
    #       if k[0] in alphabet[9:len(alphabet)] or int(k[1]) > 8:
    #           print("Invalid position detected")
    #           return False
    #
    #   print("Positions are fine.")
    #
    #   return True"""


    """~ Improved logic. ~"""

    for k, v in board.items():
        if k[0] not in 'abcdefgh' or k[1] not in '12345678' or len(k) != 2:
            print("FALSE: Invalid piece position(s)")
            return f"Invalid piece position found at '{k}', '{v}'."
        
    return "Test passed."


print(isValidChessBoard(sample_1))
print(isValidChessBoard(sample_2))
print(isValidChessBoard(sample_3))
print(isValidChessBoard(sample_4))
print(isValidChessBoard(sample_5))
