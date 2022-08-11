from getapps import now, singleday, singleweek, singleweekdays
from datetime import datetime

año, mes, dia, hora, minuto, segundo = now()

for i in range(1, 30):
    dt = datetime(año, mes, i)
    weekday = dt.weekday()
    if weekday > 4:
        print(f'{dt} es fin de semana')
    elif weekday <= 4:
        print(f'{dt} es día de semana')


# print()