# Campanario chaleco

### El objetivo principal:
 Desarrollar un sistema que permita automatizar el sistema horario del reloj cuando sucedan incovenientes que vuelven los cambios de horas inevitables; El reloj se retrasa o adelanta tiempo y deseamos que vuelva a la hora normal sin tener que hacerlo manualmente.

### El objetivo secundario 
es desarrollar una página web que permita agendar eventos y seleccionar partituras-scripts reproducibles en el campanario.

#### Metas:

> Reproducir melodías personalizadas en el campanario en horas agendadas.
> Desarrollar un control manual mediante la página web sin necesidad de tocar el hardware.
> Crear una librería para el desarrollo de partituras implementables al campanario mediante scripts.




## Postgres database setup

#### 1. Creación del directorio

En tu dirección `base (root)`, crea un directorio oculto llamado `.campanario`

Si estás en windows la dirección debería ser la siguiente:

    C:\Users\Usuario\.campanario

Usualmente en windows, las carpetas iniciando con un `.` se ocultan, por lo tanto se debería habilitar la opción de mostrar carpetas ocultas.

Si estás en linux la dirección debería ser:

    /home/usuario/.campanario

Las carpetas ocultas también deberían estar actividas en caso que quiera acceder a ellas.

#### 2. Creación del conector

Dentro del directorio, crea un archivo llamado db.py

Su contenido debería ser el siguiente:

`db.py at:`

> (linux) /home/usuario/.campanario/db.py

> (windows) C:\Users\Usuario\\.campanario\\.campanario\\db.py
<pre><code>class dbservice:
    name = 'nombre'
    user = 'usuario'
    password = 'contraseña'
    host =  'direccion'
    port = 'puerto'
</code></pre>

*El contenido cerrado entre comillas `''` será el contenido que le corresponda a la base de datos que desee conectar.*

La base de datos ya debería estar creada para ese momento. Esto es sólo para conectarse a ella.
Engine: PostgreSQL 

Una vez realizado esto, la conexión a la base de datos no debería estar expuesta.





#### 3. Creación del servicio de correo

`emailcon.py at:`

> (linux) /home/usuario/.campanario/emailcon.py

> (windows) C:\Users\Usuario\\.campanario\\.campanario\\emailcon.py
<pre><code>class emailservice:
    email='correoqueenvia@dominio'
    password='contraseñatipoapps'
    receiver='correoqueseenviaranloscodigos'
</code></pre>

*El contenido cerrado entre comillas `''` será el contenido que le corresponda a la base de datos que desee conectar.*


#### 4. Creación de las conexiones a base de datos

`connection.py at:`

> (linux) /home/usuario/.campanario/connection.py

> (windows) C:\Users\Usuario\\.campanario\\.campanario\\connection.py
<pre><code>import psycopg2 
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
    print(ex)</code></pre>
*El contenido cerrado entre comillas `''` será el contenido que le corresponda a la base de datos que desee conectar.*
