# # ¿Te has dado cuenta de que las condiciones que hemos usado hasta ahora han sido muy simples, por no decir, bastante primitivas? Las condiciones que utilizamos en la vida real son mucho más complejas. Veamos este enunciado:
# Si tenemos tiempo libre, y el clima es bueno, saldremos a caminar.
# Hemos utilizado la conjunción and (y), lo que significa que salir a caminar depende del cumplimiento simultáneo de estas dos condiciones. En el lenguaje de la lógica, tal conexión de condiciones se denomina conjunción. Y ahora otro ejemplo:
# Si tu estás en el centro comercial o yo estoy en el centro comercial, uno de nosotros le comprará un regalo a mamá.
# La aparición de la palabra or (o) significa que la compra depende de al menos una de estas condiciones. En lógica, este compuesto se llama una disyunción.
# Está claro que Python debe tener operadores para construir conjunciones y disyunciones. Sin ellos, el poder expresivo del lenguaje se debilitaría sustancialmente. Se llaman operadores lógicos.

# El operador and 
# Un operador de conjunción lógica en Python es la palabra and. Es un operador binario con una prioridad inferior a la expresada por los operadores de comparación. Nos permite codificar condiciones complejas sin el uso de paréntesis como este:
counter = 5
value = 100
counter > 0 and value == 100

# El operador or
# El operador de disyunción lógica en Python es la palabra or. Es un operador binario con una prioridad inferior a la expresada por los operadores de comparación y el operador and. Nos permite codificar condiciones complejas sin el uso de paréntesis como este:

counter > 0 or value == 100

# El operador not
# El operador de negación lógica en Python es la palabra not. Es un operador unario con una prioridad inferior a la expresada por los operadores de comparación y los operadores and y or. Nos permite codificar condiciones complejas sin el uso de paréntesis como este:

not counter > 0

# Además, hay otro operador que se puede aplicar para condiciones de construcción. Es un operador unario que realiza una negación lógica. Su funcionamiento es simple: convierte la verdad en falso y lo falso en verdad.

# Este operador se escribe como la palabra not, y su prioridad es muy alta: igual que el unario + y -. Su tabla de verdad es simple:

