'''Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
Ejemplo:
original = {"Argentina": "Buenos aires", "Chile": "Santiago"}
invertido = {"Buenos aires": "Argentina", "Santiago": "Chile"}

'''

# Definimos un diccionario de ejemplo con países y sus capitales
paises_capitales = {'Argentina': ['Buenos Aires'], 'Brasil': ['Brasilia'], 'Chile': ['Madrid']}
# Creamos un nuevo diccionario invertido
capitales_paises = {}
# Itera sobre el diccionario original
for pais, capital in paises_capitales.items():
    capitales_paises[capital[0]] = pais  # Invierte la clave y el valor
print("\nDiccionario invertido (capitales -> países):", capitales_paises)  # Imprime el nuevo diccionario