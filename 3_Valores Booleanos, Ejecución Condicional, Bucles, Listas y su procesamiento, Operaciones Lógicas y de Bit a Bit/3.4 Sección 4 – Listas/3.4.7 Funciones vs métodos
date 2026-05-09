# Imagina que estás en una cocina. Para entender la diferencia entre una **función** y un **método**, piensa en las herramientas y los ingredientes:

# ### 1. La Función: Es como una "Licuadora"

# Una función es una herramienta independiente. No le pertenece a la fruta ni a la leche; está ahí en la mesa para quien la necesite.

# * **Cómo se usa:** Metes algo dentro, la activas y te entrega un resultado.
# * **Ejemplo en código:** `jugo = licuar(fruta)`
# * **Propiedad:** Es "dueña de todo el código". Cualquier parte de tu programa puede llamarla.

# ### 2. El Método: Es como "Pelar" una naranja

# Un método es una acción que le pertenece específicamente a un objeto. No puedes "pelar" un vaso de leche, solo puedes pelar cosas que tengan cáscara (como la naranja).

# * **Cómo se usa:** Primero necesitas la fruta, pones un punto, y luego haces la acción.
# * **Ejemplo en código:** `naranja.pelar()`
# * **Propiedad:** El método es "propiedad de los datos". Está pegado al objeto y sabe cómo modificarlo.
# ---
# ### Diferencias Clave
# | Característica | Función | Método 
# | --- | --- | --- |
# | **Pertenencia** | Es independiente (global). | Le pertenece a un objeto (como una lista). |
# | **Invocación** | `nombre(dato)` | `dato.nombre()` |
# | **Efecto** | Suele crear algo nuevo sin cambiar lo original. | Puede cambiar el estado interno del objeto. |

# ### ¿Por qué es importante para las Listas?

# Como menciona tu texto, si quieres **agregar** un elemento a una lista, no usas una función suelta. Usas un método que la lista ya trae "incorporado" porque ese método tiene el permiso de alterar esa lista específica.

# * **Función (No cambia la lista):** `len(mi_lista)` -> Solo te dice cuántos hay, no toca la lista.
# * **Método (Cambia la lista):** `mi_lista.append("nuevo")` -> El método `append` entra a la lista y le pega un dato nuevo al final.

# **En resumen:** La **función** es algo que haces **con** los datos,
# mientras que el **método** es algo que el **dato sabe hacer** por sí mismo.

# ejemplo de funcion: 
tareas = ["Bordar gorra", "Estudiar Python"]

# Invocación de FUNCIÓN: El dato va DENTRO de los paréntesis
cantidad = len(tareas) 

print(cantidad) 
# Resultado en consola: 2



# ejemplo de método:
tareas = ["Bordar gorra", "Estudiar Python"]

# Invocación de MÉTODO: Se usa el PUNTO porque el método le pertenece a 'tareas'
tareas.append("Practicar inglés")

print(tareas)
# Resultado en consola: ['Bordar gorra', 'Estudiar Python', 'Practicar inglés']

# Resumen visual de la sintaxis
# Si lo ves en tu editor de código, la diferencia visual es clara:

# Función: accion(objeto) → La acción es lo principal.

# Método: objeto.accion() → El objeto es el dueño de la acción.