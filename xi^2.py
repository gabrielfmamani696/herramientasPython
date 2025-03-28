import pandas as pd
import numpy as np
from scipy.stats import chisquare

def calcular_chi_cuadrado(csv_file):
    # Leer el archivo CSV
    data = pd.read_csv(csv_file)
    
    # Verificar que existan las columnas necesarias
    if not {'observed', 'expected'}.issubset(data.columns):
      raise ValueError("El archivo CSV debe contener las columnas 'observed' y 'expected'")
    
    observed = data['observed'].values
    expected = data['expected'].values
    #print((observed-expected)^2/expected)
    s=0
    for i in range(len(observed)):
    	
      s+=(round(observed[i]-expected[i],6))**2/expected[i]
    	#print("resta: ")
    	#print(round(observed[i]-expected[i], 6))
    	print((round(observed[i]-expected[i],6))**2/expected[i])
    print(f"suma: {s}")

    #print(expected)
    # Normalizar si las sumas no coinciden
    if not np.isclose(observed.sum(), expected.sum()):
      observed = observed * (expected.sum() / observed.sum())
    
    # Calcular la prueba de chi-cuadrado
    chi2_stat, p_value = chisquare(observed, expected)
    
    return chi2_stat, p_value

# Ejemplo de uso
csv_file = "Tarea #6(Hoja1).csv"  # Reemplazar con el nombre de tu archivo
chi2_stat, p_value = calcular_chi_cuadrado(csv_file)
print(f"Chi-cuadrado: {chi2_stat}")
print(f"Valor p: {p_value}")
#Hola s