def congruencial_cuadratico(X0, a, b, c, m, iteraciones):
    secuencia = []
    Xi = X0
    for _ in range(iteraciones):
        Xi = (a * Xi**2 + b * Xi + c) % m
        ri = Xi / (m - 1)
        secuencia.append((Xi, ri))
    return secuencia

# Parámetros del ejemplo
#m minimo = 2^31
X0, a, b, c, m = 13, 26, 27, 27, 2**31
resultados = congruencial_cuadratico(X0, a, b, c, m, 100)
for i, (Xi, ri) in enumerate(resultados, 1):
  # print(f"Iteración {i}: X_i = {Xi}, r_i = {ri:.4f}")
  print(f"{ri:.4f}, ", end="")  