from datetime import datetime

# datetime object containing current date and time
fecha_actual = datetime.now()
 
print("now:", fecha_actual)



# dd/mm/YY H:M:S
dt_string = fecha_actual.strftime("%d/%m/%Y %H:%M:%S")
redondeado = int(fecha_actual.strftime("%S"))
print("date and time: ", dt_string, "redondeado: ", fecha_actual.strftime("%S"))
año_actual= fecha_actual.strftime("%Y")
mes_actual= fecha_actual.strftime("%m")
dia_actual= fecha_actual.strftime("%d")
hora_actual= fecha_actual.strftime("%H")
minuto_actual= fecha_actual.strftime("%M")
segundo_actual= fecha_actual.strftime("%S")

# print(año_actual)
# print(mes_actual)
# print(dia_actual)
# print(hora_actual)
# print(minuto_actual)
# print(segundo_actual)
