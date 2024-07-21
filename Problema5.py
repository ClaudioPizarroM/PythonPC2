#Escribe un programa que encuentre la suma de todos los números primos menores que 100

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

suma_primos = 0

for num in range(2, 100):
    if es_primo(num):
        suma_primos += num

print("La suma de todos los números primos menores que 100 es:", suma_primos)
