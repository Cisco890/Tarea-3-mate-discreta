def almacenar_en_memoria(celdas_memoria, datos):
    # Inicializar las celdas de memoria con None
    memoria = [None] * celdas_memoria

    # Función de dispersión (hashing)
    def H(n):
        return n % celdas_memoria

    # Almacenar cada dato en la memoria
    for n in datos:
        posicion = H(n)

        # Manejo de colisiones: búsqueda lineal de la siguiente posición disponible
        while memoria[posicion] is not None:
            posicion = (posicion + 1) % celdas_memoria

        memoria[posicion] = n

    return memoria

def ingresar_datos():
    while True:
        try:
            celdas_memoria = int(input("Ingrese el número de celdas de memoria: "))
            if celdas_memoria <= 0:
                raise ValueError("El número de celdas de memoria debe ser un entero positivo.")
            break
        except ValueError as e:
            print(e)
    
    while True:
        try:
            datos = list(map(int, input("Ingrese un array de números enteros separados por espacios: ").split()))
            break
        except ValueError:
            print("Todos los elementos del array deben ser números enteros.")
    
    return celdas_memoria, datos

def main():
    celdas_memoria, datos = ingresar_datos()
    resultado = almacenar_en_memoria(celdas_memoria, datos)
    print(f"Celdas de memoria después del almacenamiento: {resultado}")

if __name__ == "__main__":
    main()
