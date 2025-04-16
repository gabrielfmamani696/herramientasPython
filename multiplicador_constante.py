def obtener_centro(numero, digitos):
    """Obtiene D dígitos centrales de un número, rellenando con ceros si es necesario."""
    str_num = str(numero).zfill(2 * digitos)
    start = (len(str_num) - digitos) // 2
    return int(str_num[start:start + digitos])

def siguiente_numero(semilla, constante, digitos, estado_actual):
    """Genera el siguiente número pseudoaleatorio."""
    producto = constante * estado_actual
    nuevo_estado = obtener_centro(producto, digitos)
    return nuevo_estado, nuevo_estado  # Devuelve (número, nuevo estado)

def generar_secuencia(semilla, constante, digitos, cantidad):
    """Genera una secuencia de números pseudoaleatorios."""
    secuencia = []
    estado_actual = semilla
    for _ in range(cantidad):
        nuevo_num, estado_actual = siguiente_numero(semilla, constante, digitos, estado_actual)
        secuencia.append(nuevo_num)
    return secuencia

def generar_normalizado(semilla, constante, digitos, estado_actual):
    """Genera un número normalizado entre 0 y 1."""
    num, nuevo_estado = siguiente_numero(semilla, constante, digitos, estado_actual)
    return num / (10 ** digitos), nuevo_estado

# Ejemplo de uso con funciones
if __name__ == "__main__":
    digitos = int(input("Ingrese la cantidad de dígitos: "))
    semilla = int(input("Ingrese la semilla: "))
    constante = int(input("Ingrese la constante: "))

    
    semilla = 9803
    constante = 6965
    digitos = 4
    
    # Generar 5 números
    estado = semilla
    print("5 números pseudoaleatorios (funciones):")
    periodo = int(input("Ingrese el periodo: "))
    for _ in range(periodo):
        num, estado = siguiente_numero(semilla, constante, digitos, estado)
        # print(f"Número: {num:04d}, Estado actual: {estado}")
    
    # Generar secuencia completa
    secuencia = generar_secuencia(semilla, constante, digitos, periodo)
    secuencia_normalizada = [num / (10 ** digitos) for num in secuencia]
    print("\nSecuencia normalizada:", secuencia_normalizada)
    # print("\nSecuencia completa:", secuencia)