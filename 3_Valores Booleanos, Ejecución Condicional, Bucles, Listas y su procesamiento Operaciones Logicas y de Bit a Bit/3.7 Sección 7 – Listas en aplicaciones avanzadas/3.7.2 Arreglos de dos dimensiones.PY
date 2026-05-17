# # Supongamos también que un símbolo predefinido denominado EMPTY designa un campo vacío en el tablero de ajedrez.
# Entonces, si queremos crear una lista de listas que representan todo el tablero de ajedrez, se puede hacer de la siguiente manera:

board = []

EMPTY = input("ingrese un numero: ")

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board = [[EMPTY for i in range(8)] for j in range(8)]

# En este caso, se ha utilizado una comprensión de listas anidada para crear una lista de listas que representa el tablero de ajedrez. Cada fila del tablero se crea utilizando una comprensión de listas que genera una lista de 8 elementos, todos ellos iguales a EMPTY. Luego, la comprensión de listas externa genera 8 filas para completar el tablero.

print(board)
