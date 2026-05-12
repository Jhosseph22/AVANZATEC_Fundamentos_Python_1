# Comentamos para explicar el uso de break y continue
# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
# Se cumple la condicion entonces se activa brack para salir del ciclo y continuar conla ejecucion del programa.


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
# Salta la buelta alctual para continuar con la siguiente buelta del ciclo. 

# Diferencias entre break y continue:
# (break). Optimizar: No procesar datos innecesarios una vez que encontraste lo que buscabas 
# (continue). Filtrar: Omitir elementos que no cumplen ciertos requisitos sin detener todo el proceso

# Mas ejemplos de break

# counter = 0
# largest_number = -99999999
# while True:
#     number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
#     if number == -1:
#         break
#     counter += 1
#     if number > largest_number:
#         largest_number = number

# if counter != 0:
#     print("El número más grande es", largest_number)
# else:
#     print("No has ingresado ningún número.")


# Ejemplo de continue

largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
