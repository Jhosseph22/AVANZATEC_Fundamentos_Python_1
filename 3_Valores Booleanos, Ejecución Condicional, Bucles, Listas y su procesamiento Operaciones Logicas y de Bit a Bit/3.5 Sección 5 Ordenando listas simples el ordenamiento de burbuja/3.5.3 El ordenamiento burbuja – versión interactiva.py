# my_list = []
# swapped = True
# num = int(input("¿Cuántos elementos deseas ordenar?: "))

# for i in range(num):
#     val = float(input("Ingresa un elemento de la lista: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nOrdenada:")
# print(my_list)

# python  tiene sus propios métodos de ordenamiento, como el método sort() o la función sorted(), que son más eficientes que el método de ordenamiento de burbuja. Sin embargo, el método de ordenamiento de burbuja es un buen ejercicio para entender los conceptos básicos de los algoritmos de ordenamiento y cómo funcionan.
my_list = [8, 10, 6, 2, 4]
print("Lista original:", my_list)
my_list.sort()
print(my_list)

# Se puede usar el metodo sort() para ordenar la lista de forma ascendente, o se puede usar el argumento reverse=True para ordenar la lista de forma descendente. Por ejemplo:
my_list = [8, 10, 6, 2, 4]
print("Lista original:", my_list)
my_list.sort(reverse=True)
print(my_list)

 

