'''1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
'''

# Definimos el diccionario inicial con los precios de las frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# Añadimos las nuevas frutas con sus precios usando la asignación directa
precios_frutas['Naranja'] = 1200  # Agrego Naranja con precio 1200
precios_frutas['Manzana'] = 1500  # Agrego Manzana con precio 1500
precios_frutas['Pera'] = 2300     # Agrego Pera con precio 2300
print("Diccionario tras añadir frutas:", precios_frutas)  # Imprime el diccionario actualizado

'''2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
'''

# Actualizamos los precios de las frutas especificadas
precios_frutas['Banana'] = 1330   # Actualiza el precio de Banana a 1330
precios_frutas['Manzana'] = 1700  # Actualiza el precio de Manzana a 1700
precios_frutas['Melón'] = 2800    # Actualiza el precio de Melón a 2800
print("Diccionario tras actualizar precios:", precios_frutas)  # Imprime el diccionario actualizado

'''3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios'''

# Usamos el método keys() para obtener las claves (nombres de frutas) y convertirlas a lista
lista_frutas = list(precios_frutas.keys())  # Crea una lista con los nombres de las frutas
print("Lista de frutas:", lista_frutas)     # Imprime la lista de frutas
