'''
Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
'''
#Definicion de funciones

def decimal_a_binario(numero_decimal):
    if numero_decimal == 0:
        return "0"
    if numero_decimal == 1:
        return "1"
    return decimal_a_binario(numero_decimal // 2) + str(numero_decimal % 2)

#Menu principal

numero_decimal = int(input("Ingrese un numero decimal para pasarlo a binario: "))
print(decimal_a_binario(numero_decimal))