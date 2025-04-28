import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import csv

def leer_datos_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, newline='') as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila:  # ignorar filas vacías
                try:
                    datos.append(float(fila[0]))
                except ValueError:
                    continue  # ignorar valores no numéricos
    return np.array(datos)

def prueba_independencia_con_grafico(datos):
    n = len(datos)+2#+2 pq se 'elimina una fila''
    m = round(np.sqrt(n))
    pares = [(datos[i], datos[i+1]) for i in range(n - 1)]

    frecuencia = np.zeros((m, m))

    for x, y in pares:
        i = min(int(x * m), m - 1)
        j = min(int(y * m), m - 1)
        frecuencia[i, j] += 1

    Ei = (n - 1) / (m * m)
    chi2_observado = np.sum((frecuencia - Ei) ** 2 / Ei)

    print(f"\n📊 Resultados:")
    print(f"Total de datos (n): {n}")
    print(f"División m: {m}")
    print(f"Frecuencia esperada Ei: {Ei:.4f}")
    print(f"Chi² observado: {chi2_observado:.4f}")

    # Graficar
    x_vals, y_vals = zip(*pares)
    plt.figure(figsize=(6,6))
    plt.scatter(x_vals, y_vals, s=20, color='blue', alpha=0.7)
    plt.title(f"Pares consecutivos (n={n}) con malla {m}x{m}")
    plt.xlabel("xᵢ")
    plt.ylabel("xᵢ₊₁")

    for i in range(1, m):
        plt.axhline(i/m, color='gray', linestyle='--', linewidth=0.5)
        plt.axvline(i/m, color='gray', linestyle='--', linewidth=0.5)

    plt.grid(False)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

    return chi2_observado

# 🧪 USO
nombre_csv = "Libro 1(Hoja1).csv"
datos = leer_datos_csv(nombre_csv)
if len(datos) < 2:
    print("⚠️ El archivo debe contener al menos 2 números para formar pares.")
else:
    prueba_independencia_con_grafico(datos)
