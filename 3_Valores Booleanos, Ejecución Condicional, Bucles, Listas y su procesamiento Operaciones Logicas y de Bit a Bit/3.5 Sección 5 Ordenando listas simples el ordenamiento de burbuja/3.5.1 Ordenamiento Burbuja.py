# # Ahora veremos cómo ordenar listas simples utilizando el método de ordenamiento de burbuja. Este método es uno de los algoritmos de ordenamiento más simples y se basa en comparar elementos adyacentes y cambiarlos de posición si están en el orden incorrecto. El proceso se repite hasta que la lista esté completamente ordenada.
# # Digamos que una lista se puede ordenar de dos maneras:
# ascendente (o más precisamente - no descendente) - si en cada par de elementos adyacentes, el primer elemento no es mayor que el segundo;
# descendente (o más precisamente - no ascendente) - si en cada par de elementos adyacentes, el primer elemento no es menor que el segundo.

# En las siguientes secciones, ordenaremos la lista en orden ascendente, de modo que los números se ordenen de menor a mayor.
lista = [8, 10, 6, 2, 4]
print("Lista original:", lista)

swapped = False

my_list = [8, 10, 6, 2, 4]  # lista a ordenar

for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.

print("Lista ordenada:", my_list)

my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

# Anidamos el ciclo en otro ciclo while, que se repetirá mientras se realicen intercambios. Si no se realizan intercambios, la lista ya está ordenada y el ciclo se detendrá.


while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("lista ordenada por el ciclo while: ", my_list)

