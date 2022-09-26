import datetime
import os
import time
import sys
try:
  while (True):  
    tActual = datetime.datetime.now()
    print(f"{tActual.year}/{tActual.month}/{tActual.day}; {tActual.hour}:{tActual.minute}:{tActual.second}")
    if (tActual.minute == 55 and tActual.second == 20):
      print("La hora ha llegado :D")
      sys.exit()
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')




except KeyboardInterrupt:
  print("\nSe ha detenido el reloj mediante el teclado local")



