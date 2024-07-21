#Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
#Nota: La secuencia de Fibonacci es la serie de números:
#0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
#Cada número siguiente se obtiene sumando los dos números anteriores.



a, b = 0, 1

# Creo una lista con mi primer número de la serie
fibonacci_serie = [a]

# Itero hasta que el valor de b sea 50 o menos
while b <= 50:
    fibonacci_serie.append(b)
    a, b = b, a + b


print("Serie de Fibonacci entre 0 y 50:", fibonacci_serie)
