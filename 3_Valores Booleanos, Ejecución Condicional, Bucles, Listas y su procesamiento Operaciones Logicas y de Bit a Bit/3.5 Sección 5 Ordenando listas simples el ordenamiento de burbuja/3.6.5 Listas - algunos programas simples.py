#Ahora queremos mostrarte algunos programas simples que utilizan listas.

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)

# haciendo uso lo aprendido

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)
# En esta caso hace una compracion inecesaria del primer elemnto consigo mismos, y la idea es optimizar los recursos energeticos de las computadoras

# Haciendo uso de las rebanadas
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)
# En resumen: Comparar es como mirar un objeto; rebanar es como fotocopiar todo el inventario.

# 2. Ahora encontremos la ubicación de un elemento dado dentro de una lista:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False

for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

# Supongamos que has elegido los siguientes números en la lotería: 3, 7, 11, 42, 34, 49.
# Los números que han salido sorteados son: 5, 11, 9, 42, 3, y 49.
# La pregunta es: ¿A cuántos números le has atinado?
# Este programa te dará la respuesta:

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)