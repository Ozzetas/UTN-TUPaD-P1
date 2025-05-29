'''Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.'''

#Definicion de funciones

def suma_n_digitos(numero):
    if numero < 10:
        return numero
    return (numero % 10) + suma_n_digitos(numero // 10)

#Menu principal
numero = int(input("ingrese un numero para sumar sus digitos: "))
print(suma_n_digitos(numero))