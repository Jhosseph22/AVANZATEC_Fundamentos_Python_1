# # Python ofrece otra operación relacionada con los bits individuales: shifting. Esto se aplica solo a los valores de número entero, y no debe usar flotantes como argumentos para ello.
# Ya aplicas esta operación muy a menudo y muy inconscientemente. ¿Cómo multiplicas cualquier número por diez? Echa un vistazo:
# 12345 × 10 = 123450
# Como puede ver, multiplicar por diez es de hecho un desplazamiento de todos los dígitos a la izquierda y llenar el vacío resultante con cero.
# ¿División entre diez? Echa un vistazo:
# 12340 ÷ 10 = 1234
# Dividir entre diez no es más que desplazar los dígitos a la derecha.
# La computadora realiza el mismo tipo de operación, pero con una diferencia: como dos es la base para los números binarios (no 10), desplazar un valor un bit a la izquierda corresponde a multiplicarlo por dos; respectivamente, desplazar un bit a la derecha es como dividir entre dos (observa que se pierde el bit más a la derecha).

# Los operadores de cambio en Python son un par de dígrafos: < < y > >, sugiriendo claramente en qué dirección actuará el cambio.

valor = 1
bits = 2

valor << bits
valor >> bits

# El argumento izquierdo de estos operadores es un valor entero cuyos bits se desplazan. El argumento correcto determina el tamaño del desplazamiento.

# Esto demuestra que esta operación ciertamente no es conmutativa

# La prioridad de estos operadores es muy alta. Los verás en la tabla de prioridades actualizada, que te mostraremos al final de esta sección.

# Echa un vistazo a los turnos en la ventana del editor.

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

# 17 >> 1 → 17 // 2 (17 dividido entre 2 a la potencia de 1) → 8 (desplazarse hacia la derecha en un bit equivale a la división entera entre dos)
# 17 << 2 → 17 * 4 (17 multiplicado por 2 a la potencia de 2) → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro)

