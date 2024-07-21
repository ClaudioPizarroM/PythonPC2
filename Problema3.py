#Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
#ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
#números.
#Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
#números pares e impares.
#Ejemplo:
#“Desea ingresar un número?”: SI
#“Ingrese el número:” 5
#“¿Desea ingresar un número?”: SI
#“Ingrese el número: ” 7
#“Desea ingresar un número?”: NO
#Números ingresados: [ 5,7, 6, 7, 8, 9, 1, 2, 3, 4]
#Cantidad de números pares: 5
#Cantidad de números impares: 4
#Nota:
#- Quizás a manera de ayuda el uso de una lista le sea de utilidad.
#- El empleo de break sobre condiciones while también le serán de utilidad.

# Creo una lista para almacenar los resultados
numeros = []

# Añado 2 contadores, uno de pares e impares
pares = 0
impares = 0

while True:
    valor_ingresado = input("¿Desea ingresar un número? (SI/NO): ").strip().upper()
    
    if valor_ingresado == "SI":
        try:
            numero = int(input("Ingrese el número: "))
            numeros.append(numero)
            
            # evaluamos las condiciones
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif valor_ingresado == "NO":
        break
    else:
        print("Por favor, responda con 'SI' o 'NO'.")

# Mostrar resultados
print("\nNúmeros ingresados:", numeros)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
