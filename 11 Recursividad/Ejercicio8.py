'''
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número
'''

#Definicion de funciones
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    
    ultimo_digito = numero % 10

    if ultimo_digito == digito:
        contador = 1
    else:
        contador = 0

    return contador + contar_digito(numero // 10, digito)

#Menu principal

numero = int(input("Ingrese un numero: "))
digito = int(input("Ingrese un digito: "))

print(f"El digito {digito} aparece {contar_digito(numero,digito)} veces")