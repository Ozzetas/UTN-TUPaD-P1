'''Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).'''

contador_impar = 0
contador_negativo = 0
contador_positivo = 0
contador_par = 0

for i in range(1, 6):
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        contador_par += 1
    else:
        contador_impar += 1
    if numero > 0:
        contador_positivo += 1
    else:
        contador_negativo += 1
print(f"La cantidad de numeros negativos es: {contador_negativo}")
print(f"La cantidad de numeros positivos es: {contador_positivo}")
print(f"La cantidad de numeros pares es: {contador_par}")
print(f"La cantidad de numeros impares es: {contador_impar}")