#Escriba un programa en Python para construir el siguiente patrón.
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*


max_filas = 5

# iteramos entre los valores del 1 al 5
for i in range(1, max_filas + 1):
    print('* ' * i)

# iteramos del 5 al 1 
for i in range(max_filas - 1, 0, -1):
    print('* ' * i)
