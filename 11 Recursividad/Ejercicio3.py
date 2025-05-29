'''
Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1)
. Prueba esta función en un
algoritmo general.
'''

#Definicion de funciones

def potencia_a_la_n(num, exponente):
    if exponente == 0:
        return 1
    
    return num * potencia_a_la_n(num, exponente - 1)

#Menu principal

numero = int(input("Ingrese un numero: "))
exponente = int(input("Ingrese un exponente: "))

print(potencia_a_la_n(numero, exponente))
