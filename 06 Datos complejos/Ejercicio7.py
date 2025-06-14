'''7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
'''

# Definimos los sets de estudiantes que aprobaron cada parcial
parcial1 = {1, 2, 3, 4}  # Estudiantes que aprobaron Parcial 1
parcial2 = {3, 4, 5, 6}  # Estudiantes que aprobaron Parcial 2
# Mostramos los que aprobaron ambos parciales (intersección)
aprobados_ambos = parcial1 & parcial2  # Usa el operador & para intersección
print("Aprobaron ambos parciales:", aprobados_ambos)  # Imprime el resultado
# Mostramos los que aprobaron solo uno (diferencia simétrica)
aprobados_solo_uno = parcial1 ^ parcial2  # Usa el operador ^ para diferencia simétrica
print("Aprobaron solo uno de los parciales:", aprobados_solo_uno)  # Imprime el resultado
# Mostramos la lista total de estudiantes que aprobaron al menos uno (unión)
total_aprobados = parcial1 | parcial2  # Usa el operador | para unión
print("Total de estudiantes que aprobaron al menos un parcial:", total_aprobados)  # Imprime el resultado
