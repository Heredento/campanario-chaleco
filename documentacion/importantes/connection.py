import psycopg2 
from db import dbservice
try:
    connection=psycopg2.connect(
        host=dbservice.host,
        user=dbservice.user,
        password=dbservice.password,
        database=dbservice.name
        )
    cur = connection.cursor()    
except Exception as ex:
    print(ex)
        