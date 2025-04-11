from datetime import datetime

# Fecha de nacimiento
dia_nac = 2
mes_nac = 2  # Febrero
año_nac = 2009

# Fecha actual
dia_hoy = 11
mes_hoy = 4  # abril
año_actual = 2025

# Crear objetos datetime
fecha_nac = datetime(año_nac, mes_nac, dia_nac)
fecha_hoy = datetime(año_actual, mes_hoy, dia_hoy)

# Calcular la diferencia en días
dias_vividos = (fecha_hoy - fecha_nac).days

print(f"Días vividos: {dias_vividos}")
print(f"Años vividos: {dias_vividos // 365}")