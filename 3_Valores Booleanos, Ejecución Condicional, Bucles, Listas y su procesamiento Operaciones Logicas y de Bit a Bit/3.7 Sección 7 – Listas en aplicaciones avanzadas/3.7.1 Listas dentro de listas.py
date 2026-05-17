# Listas dento de listas

WHITE_PAWN = []
row = [WHITE_PAWN for i in range(8)]

squares = [x ** 2 for x in range(10)]

odds = [x for x in squares if x % 2 != 0 ]



print(row)
print(squares) 
print(odds)


