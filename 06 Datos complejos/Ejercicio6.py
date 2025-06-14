'''6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
Ejemplo:
alumnos = {
    "sofia":(10,9,8),
    "luis": (6, 7, 7)
}
'''

# Creamos un diccionario para almacenar los nombres y sus tuplas de notas
alumnos = {}
# Bucle para ingresar 3 alumnos con sus notas
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")  # Solicita el nombre
    nota1 = float(input(f"Ingrese la primera nota de {nombre}: "))  # Solicita la primera nota
    nota2 = float(input(f"Ingrese la segunda nota de {nombre}: "))  # Solicita la segunda nota
    nota3 = float(input(f"Ingrese la tercera nota de {nombre}: "))  # Solicita la tercera nota
    alumnos[nombre] = (nota1, nota2, nota3)  # Almacena la tupla de notas
# Calculamos e imprimimos el promedio de cada alumno
for nombre, notas in alumnos.items():  # Itera sobre el diccionario
    promedio = sum(notas) / len(notas)  # Calcula el promedio
    print(f"El promedio de {nombre} es: {promedio:.2f}")  # Imprime el promedio con 2 decimales