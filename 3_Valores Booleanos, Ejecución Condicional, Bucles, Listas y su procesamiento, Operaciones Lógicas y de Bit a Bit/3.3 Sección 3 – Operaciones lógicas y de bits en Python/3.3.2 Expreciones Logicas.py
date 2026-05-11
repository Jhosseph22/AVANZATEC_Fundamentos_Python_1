var = 1
# Creamos una variable llamada var y asignemosle 1, las siguientes condiciones son equivalenste a pares
print(var > 0) # var es mayor que 0
print(not (var<=0)) # var no es menor o igual a 0

# ejemplo 2
print(var != 0)
print(not (var == 0))

# # Puedes estar familiarizado con las leyes de De Morgan. Dicen que:

# La negación de una conjunción es la separación de las negaciones.

# La negación de una disyunción es la conjunción de las negaciones.

# Escribamos lo mismo usando Python:
p = True
q = False

not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)

print(not (p and q) == (not p) or (not q))
print(not (p or q) == (not p) and (not q))
