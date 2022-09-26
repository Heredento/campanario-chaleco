import os, sys
sys.path.append(os.path.join(os.path.expanduser('~'), '.campanario'))
from connection import cur, connection
query = f"update paginaweb_ClockInformation set is_active=false where name='server_active';"
cur.execute(query)
connection.commit()
command = '. env/bin/activate;python3 campanario/manage.py makemigrations;python3 campanario/manage.py migrate'
os.system(command)