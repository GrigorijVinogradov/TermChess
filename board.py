import pieces

size = 8 

square_pairing = pieces.white_square + " " +pieces.black_square

while(size > 0):
    print(f"{size} " + (square_pairing + " ") * 4)
    size -= 1
    square_pairing = square_pairing[::-1]

print("  A B C D E F G H")
