# # Cualquier elemento de la lista puede ser eliminado en cualquier momento - esto se hace con una instrucción llamada del (eliminar). Nota: es una instrucción, no una función.
# Tienes que apuntar al elemento que quieres eliminar - desaparecerá de la lista y la longitud de la lista se reducirá en uno.
# Mira el fragmento de abajo. ¿Puedes adivinar qué output producirá? Ejecuta el programa en el editor y comprueba.

numbers = [10, 5, 7, 2, 1]
del numbers[1]
print(len(numbers))
print(numbers)

# No puedes acceder a un elemento que no existe - no puedes obtener su valor ni asignarle un valor. Ambas instrucciones causarán ahora errores de tiempo de ejecución:

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

###

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

print(numbers[4])
numbers[4] = 1
