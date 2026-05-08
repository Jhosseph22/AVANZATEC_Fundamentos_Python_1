# # La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.

# Se puede usar tanto con bucles while y for.
# Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:
# un bucle for;
# el concepto de ejecución condicional (if-elif-else).
# la sentencia continue.
# Tu programa debe:

# pedir al usuario que ingrese una palabra.
# utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados 
# métodos de cadena y el método upper() muy pronto, no te preocupes
# utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
# imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada
# Prueba tu programa con los datos que le proporcionamos.

user_word = str(input("Ingresa una palabra: "))
user_word = user_word.upper()  # Convierte la palabra ingresada a mayúsculas


for letter in user_word:
   if letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
        continue  # Si la letra es una vocal, omite el resto del código en esta iteración y pasa a la siguiente letra
   elif letter != "A" and letter != "E" and letter != "I" and letter != "O" and letter != "U":
       print(letter)
   else:
        print("Error: No hay consonantes en la palabra ingresada", letter)   