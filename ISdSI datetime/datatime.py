from datatime import datetime

ahora = datetime.now()

print(ahora.year) # Año de hoy
print(ahora.strftime('%A')) #dia de hoy

fecha = datetime(2025, 10, 4)
print(fecha.strftime('%B')) # Mes de una fecha

str_fecha = '11/04/25 14:58:00'
fecha_obj= datetime.strptime(str_fecha,'%d/%m/%y %H:%s')
