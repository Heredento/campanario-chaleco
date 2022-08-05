### Postgres database setup

#### 1. Creación del directorio

En tu dirección base, crea un directorio oculto llamado `.campanario`

Si estás en windows la dirección debería ser la siguiente:

    C:\Users\Usuario\.campanario

Usualmente en windows, las carpetas iniciando con un `.` se ocultan, por lo tanto se debería habilitar la opción de mostrar carpetas ocultas.

Si estás en linux la dirección debería ser:

    /home/usuario/.campanario

Las carpetas ocultas también deberían estar actividas en caso que quiera acceder a ellas.

#### 2. Creación del conector

Dentro del directorio, crea un archivo llamado db.py

Su contenido debería ser el siguiente:
<pre><code>
class dbservice:
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