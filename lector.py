print("=== Iniciando Lector de Diccionarios ===")

# Abrimos el archivo de texto en modo lectura ('r')
with open("diccionario_prueba.txt", "r") as archivo:
    contador = 0
    for linea in archivo:
        contador += 1
        # Eliminamos los saltos de linea invisibles (\n)
        contrasena = linea.strip()
        print(f"Clave {contador}: {contrasena}")

print("=========================================")
print(f"Proceso terminado. Se leyeron {contador} contrasenas.")
