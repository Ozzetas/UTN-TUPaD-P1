'''
Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
'''

#Definicion de funciones

def contar_bloques(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return numero + contar_bloques(numero - 1)

#Menu principal

numero_bloques = int(input("Ingrese el numero de bloques inferior: "))

print(f"El numero total de bloques necesarios para construir la piramide es: {contar_bloques(numero_bloques)}")
