# Un nuevo elemento puede ser añadido al final de la lista existente:
value = 4
list = [1, 2, 3]
print(list)  # Resultado en consola: [1, 2, 3]

list.append(value)
print(list)  # Resultado en consola: [1, 2, 3, 4]

# Dicha operación se realiza mediante un método llamado append(). Toma el valor de su argumento y lo coloca al final de la lista que posee el método.

# La longitud de la lista aumenta en uno.

# El método insert() es un poco más inteligente - puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.

location = 2
value = 5
list.insert(location, value)
print(list)  # Resultado en consola: [1, 2, 5, 3, 4]


# el elemento incertado desplaza a los elementos que estaban en esa posición y a los siguientes, hacia la derecha.
# ejemplo
numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
numbers.insert(1, 333)


print(len(numbers))
print(numbers)

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

# modifivando el código para usar insert en lugar de append, y así agregar los elementos al inicio de la lista:

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)

