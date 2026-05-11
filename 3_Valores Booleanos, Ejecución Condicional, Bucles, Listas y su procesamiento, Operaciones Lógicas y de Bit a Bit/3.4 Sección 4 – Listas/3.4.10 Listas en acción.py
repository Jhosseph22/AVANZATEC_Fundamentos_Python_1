# Como usamos las listas en programacion
# Aprendí que Power Soul Se puede Cambiar La extensión de los archivos cuando los archivos no tienen extensión

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# Se ve bien con cinco elementos.

# ¿Seguirá siendo aceptable con una lista que contenga 100 elementos? No, no lo hará.

# ¿Puedes usar el bucle for para hacer lo mismo automáticamente, independientemente de la longitud de la lista? Si, si puedes.

# Así es como lo hemos hecho:
my_list = [10, 1, 8, 3, 5, 7, 9, 2, 6, 4]
length = len(my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

