#Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
#en el rango de 1500 y 2700 (ambos incluidos).

# creo una lista en blanco para almacenar mis resultados
numeros_encontrados = []

# itero entre los valores solicitados
for numero in range(1500, 2701):
    # Verificamos condiciones de divisor y multiplo
    if numero % 7 == 0 and numero % 5 == 0:
        numeros_encontrados.append(numero)

print("Números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(numeros_encontrados)
