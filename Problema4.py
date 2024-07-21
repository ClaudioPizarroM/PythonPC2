#Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
#pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
#materias.
#Puede usar el siguiente esquema a manera de ejemplo
#{
#Alumno: Juan,
#Notas: [10, 12, 15]
#}
#Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
#completo de los alumnos.
#Nota:
#El uso de listas con diccionarios le será de utilidad.



alumnos = []

num_alumnos = int(input("Ingrese el número de alumnos: "))

# Iteramos para añadir los datos solicitados
for _ in range(num_alumnos):
    alumno = {}
    alumno["Nombre"] = input("Ingrese el nombre del alumno: ")
    alumno["Notas"] = []
    
    # Ingresamos los valores de las notas con otro bucle para que se añaden 3 notas, además le he puesto una condicional para que solo puedan ser notas de 0 a 20
    for i in range(1, 4):
        while True:
            nota = float(input(f"Ingrese la calificación {i} de {alumno['Nombre']}: "))
            if 0 <= nota <= 20:
                alumno["Notas"].append(nota)
                break
            else:
                print("Calificación inválida. Por favor, ingrese un valor entre 0 y 20.")
    
    
    alumnos.append(alumno)

# Imprimimos los resultados de las listas
print("\nListado de alumnos y sus calificaciones:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Nombre']}, Notas: {alumno['Notas']}")

