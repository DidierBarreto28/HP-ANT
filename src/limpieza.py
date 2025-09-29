import os

# Rutas
ruta_raw = r"C:\DB_Safe\Future\Projects\HP-ANT\data.raw\hospitales_antioquia.csv"
ruta_clean = r"C:\DB_Safe\Future\Projects\HP-ANT\data.processed\hospitales_antioquia_limpio.csv"

# Leer el archivo original
with open(ruta_raw, "r", encoding="utf-8") as f:
    contenido = f.read()

# 🔧 Reemplazar comillas dobles extra "" por una sola "
contenido = contenido.replace('""', '"')

# Guardar versión corregida
with open(ruta_clean, "w", encoding="utf-8") as f:
    f.write(contenido)

print(f"✅ Archivo limpio guardado en: {ruta_clean}")
