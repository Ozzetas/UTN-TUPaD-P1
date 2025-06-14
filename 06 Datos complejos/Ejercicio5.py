'''
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
Ejemplo:
#Entrada -> "Hola mundo hola"
#Salida:
Palabras_unicas: {'hola', 'mundo'}
Recuento: {'hola': 2, 'mundo': 1}
'''

# Solicitamos una frase al usuario
frase = input("Ingrese una frase: ")  # Pide una frase
# Convertimos la frase a minúsculas y la dividimos en palabras
palabras = frase.lower().split()  # Divide la frase en lista de palabras
# Creamos un set para obtener palabras únicas
palabras_unicas = set(palabras)  # Convierte la lista en un set para eliminar duplicados
print("Palabras únicas:", palabras_unicas)  # Imprime las palabras únicas
# Creamos un diccionario para contar la frecuencia de cada palabra
conteo_palabras = {}
for palabra in palabras:  # Itera sobre cada palabra
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1  # Incrementa el contador
print("Conteo de palabras:", conteo_palabras)  # Imprime el diccionario de frecuencias