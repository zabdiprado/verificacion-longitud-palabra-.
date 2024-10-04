def contar_vocales_consonantes(palabra):
    vocales = "aeiouAEIOU"
    contador_vocales = 0
    contador_consonantes = 0

    for letra in palabra:
        if letra.isalpha():  # Verifica si es una letra
            if letra in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1

    return contador_vocales, contador_consonantes

def verificar_longitud_palabra():
    print("¡Bienvenido al programa de verificación de longitud de palabras!")
    print("Puedes ingresar palabras de entre 4 y 8 letras, o 'salir' para terminar.\n")

    while True:  # Permitir que el usuario ingrese varias palabras
        palabra = input("Ingresa una palabra (o 'salir' para terminar): ")

        if palabra.lower() == 'salir':  # Opción para salir del bucle
            print("Saliendo del programa. ¡Hasta luego!")
            break

        if not palabra.isalpha():  # Validación de entrada
            print("Por favor, ingresa solo letras.")
            continue  # Volver a pedir la palabra

        longitud = len(palabra)

        # Verificar la longitud de la palabra
        if 4 <= longitud <= 8:
            print("La palabra es correcta.")
        elif longitud < 4:
            print(f"Hacen falta letras. Solo tiene {longitud} letras.")
        else:
            print(f"Sobran letras. Tiene {longitud} letras.")

        # Contar vocales y consonantes
        vocales, consonantes = contar_vocales_consonantes(palabra)
        print(f"La palabra tiene {vocales} vocal(es) y {consonantes} consonante(s).\n")

# Llamar a la función
verificar_longitud_palabra()
