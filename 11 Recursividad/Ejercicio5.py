'''
Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
'''

#Definicion de funciones
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0].lower() != palabra[-1].lower():
        return False
    return es_palindromo(palabra[1:-1])

#Menu principal
palabra = input("Ingrese una palabra para verificar si es palindromo: ")
print(f"La palabra {palabra} es palindromo? {es_palindromo(palabra)}")
