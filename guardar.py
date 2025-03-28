iteracion = 0    
with open("iteracion.txt", "r") as archivo:
  numero_leido = int(archivo.read())  # Convierte el texto a un número entero
  iteracion = numero_leido
print(f"iteracion actual: {numero_leido}")

iteracion += 1
with open("iteracion.txt", "w") as archivo:
  archivo.write(str(iteracion))  # Convertimos el número a string antes de escribirlo

print(f"siguiente iteracion: {iteracion}")
