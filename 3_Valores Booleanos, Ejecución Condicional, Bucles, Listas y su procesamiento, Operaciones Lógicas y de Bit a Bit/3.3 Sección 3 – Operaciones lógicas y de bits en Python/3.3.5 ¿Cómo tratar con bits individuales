# Ahora te mostraremos para que puedes usar los operadores de bit a bit. Imagina que eres un desarrollador obligado a escribir una pieza importante de un sistema operativo. Se te ha dicho que puedes usar una variable asignada de la siguiente forma:
# mascara es una herramienta que tapa todo lo demas( en mis palabras coloca un 1 en la posision que se quiere conocer su valor
# luego realizacmos una compracion y analizamos el resultado

numero = 13      # Binario: 1101
posicion = 2     # El tercer bit (0, 1, 2)

# Creamos un 1 y lo movemos a la posición deseada
mask = 1 << posicion  

# Comparamos. Si el bit en 'numero' era 0, 0 & 1 dará 0.
# Si el bit era 1, 1 & 1 dará algo mayor a 0.
if (numero & mask) > 0:
    print(f"El bit en la posición {posicion} está ENCENDIDO (1)")
else:
    print(f"El bit en la posición {posicion} está APAGADO (0)")