'''Escribir un programa que tome la lista
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma:
import random
numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
'''

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

#Sesgo positivo a la derecha:
if media > mediana and mediana > moda:
    print("Hay sesgo positivo a la derecha.")
#Sesgo negativo o a la izquierda
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo o a la izquierda.")
#Sin sesgo
elif media == mediana and media == moda:
    print("Sin sesgo")
else:
    print("No se cumple ninguna de las 3 codiciones.")