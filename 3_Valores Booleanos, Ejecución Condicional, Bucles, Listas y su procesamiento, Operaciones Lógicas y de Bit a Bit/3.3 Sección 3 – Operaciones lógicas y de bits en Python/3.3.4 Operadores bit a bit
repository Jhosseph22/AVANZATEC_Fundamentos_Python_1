# # Sin embargo, hay cuatro operadores que le permiten manipular bits de datos individuales. Se denominan operadores bit a bit.

# Cubren todas las operaciones que mencionamos anteriormente en el contexto lógico, y un operador adicional. Este es el operador xor (significa o exclusivo ), y se denota como ^ (signo de intercalación).

# Aquí están todos ellos:

# & (ampersand) ‒ conjunción a nivel de bits;
# | (barra vertical) - disyunción a nivel de bits;
# ~ (tilde) - negación a nivel de bits;
# ^ (signo de intercalación) - o exclusivo a nivel de bits (xor).

# Los operadores bit a bit son más estrictos: tratan con cada bit por separado. 
# Si asumimos que la variable entera ocupa 64 bits (lo que es común en los sistemas informáticos modernos), 
# puede imaginar la operación a nivel de bits como una evaluación de 64 veces del operador lógico para cada 
# par de bits de los argumentos. Su analogía es obviamente imperfecta, ya que en el mundo real todas 
# estas 64 operaciones se realizan al mismo tiempo (simultáneamente).

i = 15
j = 22

log = i and j
print(bool(log))

bit = i & j
print(bool(bit))

logneg = not i
print(bool(logneg))


bitneg = ~i
print(bool(bitneg))
print(f"{bitneg:064b}")
print(int(f"{bitneg:064b}", 2))

numero = 10
print(f"{numero:064b}") 

# Formas abreviadas de escribir operadores bit a bit

x = True
y = True

x = x & y # es lo mismo que x &= y
x = x | y # es lo mismo que x |= y
x = x ^ y # es lo mismo que x ^= y

x &= y
x |= y
x ^= y

print(x, y)

