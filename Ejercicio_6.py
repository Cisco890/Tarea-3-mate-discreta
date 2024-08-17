def generar_pseudoaleatorios(m, a, c, s, n):
    # Validaciones de las condiciones requeridas
    if not (2 <= a < m):
        raise ValueError("El multiplicador 'a' debe satisfacer 2 ≤ a < m.")
    if not (0 <= c < m):
        raise ValueError("El incremento 'c' debe satisfacer 0 ≤ c < m.")
    if not (0 <= s < m):
        raise ValueError("La semilla 's' debe satisfacer 0 ≤ s < m.")
    
    # Inicializar la sucesión pseudoaleatoria
    x = [0] * n
    x[0] = s
    
    # Generar la sucesión utilizando la fórmula congruencial
    for i in range(1, n):
        x[i] = (a * x[i-1] + c) % m
    
    return x

def ingresar_datos():
    while True:
        try:
            m = int(input("Ingrese el valor del módulo m: "))
            a = int(input("Ingrese el valor del multiplicador a: "))
            c = int(input("Ingrese el valor del incremento c: "))
            s = int(input("Ingrese el valor de la semilla s: "))
            n = int(input("Ingrese la cantidad de números pseudoaleatorios a generar: "))
            break
        except ValueError:
            print("Todos los valores deben ser enteros. Por favor, intente de nuevo.")
    
    return m, a, c, s, n

def main():
    m, a, c, s, n = ingresar_datos()
    try:
        resultado = generar_pseudoaleatorios(m, a, c, s, n)
        print(f"Secuencia de números pseudoaleatorios generada: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
