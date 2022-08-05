from datetime import datetime

try:
    fecha_actual = datetime.now()
    dt = fecha_actual.strftime("%d/%m/%Y | %H:%M:%S")
finally:
    fecha_actual = datetime.now()
    dt = fecha_actual.strftime("%d/%m/%Y | %H:%M:%S")