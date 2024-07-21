#Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
#por ejemplo, omitiendo las vocales.
#Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
#texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
#minúsculas.
#Ejemplo:
#- Input: Twitter Output: Twttr
#- Input: What's your name? Output: Wht's yr nm?

def eliminar_vocales(texto):
    
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    
    # Reemplazar cada vocal con una cadena vacía
    for vocal in vocales:
        texto = texto.replace(vocal, "")
    
    return texto

texto_usuario = input("Ingrese una cadena de texto: ")

# Eliminar las vocales de la cadena de texto
texto_abreviado = eliminar_vocales(texto_usuario)

# Imprimir la cadena de texto sin vocales
print("Texto sin vocales:", texto_abreviado)

