# - PASSPAGE - #
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
    print("Conexión exitosa!")

    
except Exception as ex:
    print(ex)


# - PASSPAGE - #

class emailservice:
    email='correoqueenvia@dominio'
    password='contraseñatipoapps'
    receiver='correoqueseenviaranloscodigos'

# - PASSPAGE - #

class dbservice:
    name ='campanariodb'
    user ='campanariosudo'
    password= '20160176'
    host =  '127.0.0.1'
    port = '5432'
