import matplotlib.pyplot as plt
import math

# Datos
lista = [11, 11, 11, 12, 14, 10, 2, 14, 12, 9, 9, 14, 9, 10, 13, 7, 4, 12, 9, 6, 15, 8, 11, 8, 12, 6, 8, 6, 15, 14]


# Cálculos iniciales
media = sum(lista)/len(lista)
print(f'Media: {media}')

# Media redondeada
lambdax = round(media)
print(f'Media redondeada: {lambdax}')

variancia_muestral = 0
for numero in lista:
    variancia_muestral += (numero - media)**2
variancia_muestral = variancia_muestral/(len(lista)-1)
print(f'Varianza muestral: {variancia_muestral}')
print(f'Mínimo: {min(lista)}')
print(f'Máximo: {max(lista)}')

# Parámetros
minimo = min(lista)
maximo = max(lista)
ancho_intervalo = round((maximo - minimo)/round(math.sqrt(len(lista))))
print(f'Ancho de intervalo: {ancho_intervalo}')

# Generar intervalos
intervalos_bordes = []
inicio = minimo
while inicio <= maximo:
    fin = inicio + ancho_intervalo - 1
    intervalos_bordes.append((inicio, min(fin, maximo)))  # No pasarse del máximo
    inicio += ancho_intervalo

# Inicializar contadores
conteo_intervalos = {f'{inicio}-{fin}': 0 for inicio, fin in intervalos_bordes}

# Contar datos
for numero in lista:
    for inicio, fin in intervalos_bordes:
        if inicio <= numero <= fin:
            conteo_intervalos[f'{inicio}-{fin}'] += 1
            break

# Preparar datos para graficar
etiquetas = list(conteo_intervalos.keys())
frecuencias = list(conteo_intervalos.values())

# Función de Poisson
def poisson(k, lambd):
    return (math.exp(-lambd) * lambd**k) / math.factorial(k)

# Calcular probabilidades de Poisson para cada intervalo
poisson_intervalos = {}

for inicio, fin in intervalos_bordes:
    probabilidad = 0
    for k in range(inicio, fin + 1):
        probabilidad += poisson(k, round(media))
    poisson_intervalos[f'{inicio}-{fin}'] = probabilidad

# Mostrar resultados de conteo y Poisson
print(f'Conteo de intervalos: {conteo_intervalos}')
print(f'Probabilidades Poisson por intervalo: {poisson_intervalos}')

# Graficar el histograma de frecuencias y las probabilidades de Poisson
frecuencia_poisson = list(poisson_intervalos.values())

plt.figure(figsize=(10, 6))

# Graficar las frecuencias observadas (histograma)
plt.bar(etiquetas, frecuencias, width=0.6, color='skyblue', edgecolor='black', alpha=0.6, label='Frecuencia Observada')

# Graficar las probabilidades de Poisson para los intervalos
plt.plot(etiquetas, frecuencia_poisson, color='red', marker='o', label='Poisson Esperada')

plt.xlabel('Intervalos')
plt.ylabel('Frecuencia')
plt.title('Histograma de Frecuencias Observadas vs Probabilidades de Poisson')
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

print(poisson_intervalos.values())

it = 0
for i in poisson_intervalos.values():
    print(f'E{it}: {i}*{len(lista)}={i*len(lista)}')
    print(f'Error{it}: {i}*{len(lista)}={i*len(lista)}')
    it += 1
