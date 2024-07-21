#En los Estados Unidos, las fechas suelen tener el siguiente formato: mes-día-año (MM/DD/AAAA). Las
#fechas en ese formato no se pueden ordenar fácilmente porque el año de la fecha es el último en
#lugar del primero. Intente ordenar, por ejemplo, 2/2/1800, 3/3/1900 y 1/1/2000 cronológicamente
#en cualquier programa (por ejemplo, una hoja de cálculo). Las fechas en ese formato también son
#ambiguas. ¡Una fecha como el 8 de septiembre de 1636, podría interpretarse como el 9 de agosto de
#1636!
#Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
#8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
#la lista abajo:
#[
#"Enero",
#"Febrero",
#"Marzo",
#"Abril",
#"Mayo",
#"Junio",
#"Julio",
#"Agosto",
#"Septiembre",
#"Octubre",
#"Noviembre",
#"Diciembre"
#]
#Luego, genere esa misma fecha en formato AAAA-MM-DD.
#Ejemplos:
#- Input: 9/8/1636 | Output: 1636-09-08
#- Input: Septiembre 8, 1636 | Output: 1636-09-08
#- Input: 1/1/1970 | Output: 1970-01-01
#Nota:
#- Los métodos de listas y string le resultarán de gran utilidad.
#- Nota que si empleamos print(f"{n:02}") , esta completará con 0 valos a la izquierda de un
#número

def convertir_fecha(fecha):
    
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    if '/' in fecha:
        mes, dia, anio = fecha.split('/')
    elif ',' in fecha:
        mes_nombre, dia_anio = fecha.split(' ', 1)
        dia, anio = dia_anio.split(', ')
        mes = meses.index(mes_nombre) + 1
    else:
        return "Formato de fecha no reconocido"

    mes = int(mes)
    dia = int(dia)
    anio = int(anio)
    
    mes = f"{mes:02}"
    dia = f"{dia:02}"
    anio = f"{anio}"

    return f"{anio}-{mes}-{dia}"

fecha_usuario = input("Ingrese una fecha, por favor: ")

fecha_convertida = convertir_fecha(fecha_usuario)

print("Fecha en formato YYYY-MM-DD:", fecha_convertida)
