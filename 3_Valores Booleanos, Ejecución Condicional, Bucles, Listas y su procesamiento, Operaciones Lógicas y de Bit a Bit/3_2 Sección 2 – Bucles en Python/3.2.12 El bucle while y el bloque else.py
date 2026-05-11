# # Ambos bucles while y for, tienen una característica interesante (y rara vez se usa).
# Te mostraremos como funciona - intenta juzgar por ti mismo si es utilizable.
# En otras palabras, trata de convencerte si la función es valiosa y útil, o solo es azúcar sintáctica.
# Echa un vistazo al fragmento en el editor. Hay algo extraño al final - la palabra reservada else.
# Como pudiste haber sospechado, los bucles también pueden tener la rama else, como los if.
# La rama else del bucle siempre se ejecuta una vez, independientemente de si el bucle ha entrado o no en su cuerpo.
# ¿Puedes adivinar la output? Ejecuta el programa para comprobar si tenías razón.

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
