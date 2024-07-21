#Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número
#perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
#(excluyendo el propio número).
#Ejemplo Identificar número perfecto:
#Número perfecto: 6
#● Divisores propios: 1, 2, 3
#● Suma de los divisores propios: 1 + 2 + 3 = 6

def es_num_perfecto(n):
    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

numeros_perfectos = []

for num in range(1, 1000):
    if es_num_perfecto(num):
        numeros_perfectos.append(num)

# Imprimir los números perfectos encontrados
print("Números perfectos menores que 1000:", numeros_perfectos)

