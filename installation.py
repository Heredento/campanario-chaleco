import os, sys

command='''
python3 -m venv env;
. env/bin/activate; 
pip install -r requirements.txt;
python3 campanario/manage.py makemigrations;
python3 campanario/manage.py migrate; 
'''  

sys.path.append(os.path.join(os.path.expanduser('~'), '.campanario'))
from connection import cur, connection
print("\nIniciando conexión a la base de datos")
try:
    query = f"update paginaweb_ClockInformation set is_active=false where name='server_active';"
    cur.execute(query)
    connection.commit()
    print("Conexión a la base de datos exitosa!")
except Exception as ex:
    print("Sucedió un problema con la conexión de la base de datos.")
    print(f"ERROR: {ex}")
    print("Si es la primera vez instalando ignorar el problema")
print("\nIniciando proceso de instalación de paquetes y migración...")
try:
    os.system(command)
except Exception as ex:
    print("Sucedió un problema con la instalación de paquetes o migración..")
    print(f"ERROR: {ex}")
