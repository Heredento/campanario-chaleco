
#### Aclaraciones
Los siguientes archivos son vitales para la página web pero dejarlos al descubierto dentro github es lo que he deseado no realizar, debido a ello se crean estos archivos.

#### 1.1. Creación del directorio

En tu dirección `base (root)`, crea un directorio oculto llamado `.campanario`

El directorio debería verse como debería ser:

> /home/usuario/.campanario

Las carpetas ocultas también deberían estar activadas en caso que quiera acceder a ellas.

#### 1.2. Creación del conector

Dentro del directorio, crea un archivo llamado `db.py`
El directorio debería verse como:
> /home/usuario/.campanario/db.py

Su contenido debería ser el siguiente:

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





#### 1.3. Creación del servicio de correo

`archivo: emailcon.py`

> /home/usuario/.campanario/emailcon.py

<pre><code>class emailservice:
    email='correoqueenvia@dominio'
    password='contraseñatipoapps'
    receiver='correoqueseenviaranloscodigos'
</code></pre>

*El contenido cerrado entre comillas `''` será el contenido que le corresponda a la información que será utilizada, información mál probada no funcionará.*


#### 1.4. Creación de las conexiones a base de datos

`archivo: connection.py`

> /home/usuario/.campanario/connection.py

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

except Exception as ex:
    print(ex)</code></pre>

*Este contenido facilita importar acciones dentro de la página, este no es necesario que se realicen cambios.*

#### 1.5. Llave secreta de la página web

`archivo: secretkey.py`

> /home/usuario/.campanario/secretkey.py

Una vez creado el archivo, por favor abrir el siguiente enlace, generar un código, copiarlo y pegarlo entre los parentesis de `key = 'aquí'`

[Generador de llaves secretas de DJANGO](https://djecrety.ir/)

Esta llave se usa para muchas funciones internas y no debería poseerlo cualquier persona, esto es de suma importancia.

<pre><code>class djangokey:
        key = 'llave secreta obtenida'</code></pre>
