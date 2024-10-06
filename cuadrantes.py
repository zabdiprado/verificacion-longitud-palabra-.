# Definimos una función para determinar el cuadrante
def determinar_cuadrante(x, y):
    if x > 0 and y > 0:
        return "El punto se encuentra en el cuadrante I"
    elif x < 0 and y > 0:
        return "El punto se encuentra en el cuadrante II"
    elif x < 0 and y < 0:
        return "El punto se encuentra en el cuadrante III"
    elif x > 0 and y < 0:
        return "El punto se encuentra en el cuadrante IV"

# Esta es la función principal del programa
def main():
    # Pedimos al usuario que ingrese su nombre
    nombre = input("¡Hola! ¿Cuál es tu nombre? ")
    
    # Saludamos al usuario
    print(f"Hola , {nombre}!")

    # Pedimos al usuario que ingrese las coordenadas
    x = float(input("Ingrese X: "))
    y = float(input("Ingrese Y: "))

    # Verificamos que las coordenadas no sean cero
    if x == 0 or y == 0:
        print("Error: Ninguna coordenada puede ser 0.")
    else:
        # Llamamos a la función para determinar el cuadrante
        resultado = determinar_cuadrante(x, y)
        # Mostramos el resultado
        print(resultado)

# Este es el punto de entrada del programa
if __name__ == "__main__":
    main()
