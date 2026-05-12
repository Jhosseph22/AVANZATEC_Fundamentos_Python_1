# Pregunta 1: ¿Cuál es el resultado del siguiente fragmento de código?
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))

# Pregunta 2: ¿Cuál es el resultado del siguiente fragmento de código?

x = 4
y = 1

print(f"{x:03b}")
print(f"{y:03b}")


a = x & y
b = x | y
c = ~x  # ¡difícil!
d = x ^ 5
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)

