# Observa el fragmento de código a continuación:

# my_list[start:end]
 
# Para confirmar:

# start es el índice del primer elemento incluido en la rebanada.
# end es el índice del primer elemento no incluido en la rebanada.
# Así es como los índices negativos funcionan en las rebanadas:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

# Funcion del con rebanadas
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

# Eliminar todos los elementos a la vez
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
