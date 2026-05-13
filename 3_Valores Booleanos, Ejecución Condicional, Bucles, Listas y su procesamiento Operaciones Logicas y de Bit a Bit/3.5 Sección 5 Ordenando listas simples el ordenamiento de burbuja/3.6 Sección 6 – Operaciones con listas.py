# como procesar listas usando rebanadas y operadores in y not in
list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

# El programa:
# crea una lista de un elemento llamada list_1;
# la asigna a una nueva lista llamada list_2;
# cambia el único elemento de list_1;
# imprime la list_2;

list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)



# Una de las formas más generales de la rebanada es la siguiente:
# my_list[inicio:fin] 

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)



