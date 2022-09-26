# CAMPANARIO CHALECO

TUTORIAL COMPLETO DE INSTALACIÓN [AQUÍ](https://youtu.be/P4Zgwv5exEQ)

### OBJETIVOS

 Restablecer la hora del reloj cuando sucedan cortes de energía.

- [x] Desarrollar un página web personalizada con las siguientes funciones:
    1. Crear un sistema que permita implementar canciones mediante scripts programables que utilicen teoría musical. [LEER MÁS](./documentacion/instrucciones/song_creator.md)
    2. Programar las situaciones para que una canción se puede reproducir a lo largo de todo el año dentro de la página web.
    3. Programar el tiempo en que las luces de las agujas del reloj se enciendan.
- [x] Redactar documentación necesaria para la implementación del sistema.

### IMPORTANTE

El sistema se apoya en linux con Raspberry Pi, muchas capacidades está limitadas a sus funciones internas de GPIO, no funcionará de igual forma en una PC que tenga Windows o incluso Linux instalado. Sólo para Raspberry Pi 3B+ o mayor.

<hr>

### [1. Configuración de archivos dependentes importantes](./documentacion/instrucciones/setup_dependencies.md)

### [2. Sistema de creación de canciones](./documentacion/instrucciones/song_creator.md)

### [3. Resumen de la estructura](./documentacion/estructura-documentacion.md)

<hr>## Configurar el sistema y la página web en una nueva Raspberry Pi
- Instalar Raspberry OS en la Raspberry [Tutorial práctico](https://youtu.be/cSx-5YJnFRI)
- En la terminal recomendamos escribir los siguientes comandos:
<code><pre>sudo apt update; sudo apt upgrade;</code></pre>

- Haber instalado una version de python mayor o igual a 3.10.

    Para instalar python recomendamos seguir las siguientes instrucciones:

    Descargar el instalador comprimido en la página oficial de python.  [LEER MÁS](https://www.python.org/downloads/source/)

    La versión que utilizo en el video es Python 3.10.7 [Enlace directo aquí](https://www.python.org/downloads/release/python-3107/)
    
    1. Documentación para instalar python en Linux. [LEER MÁS](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-ubuntu-20-04-quickstart-es)

    2. Instalación de independencias:
    <pre>sudo apt install build-essential libssl-dev libffi-dev python3-dev</pre>
    
    3. Generar el instalador y configurar las optimizaciones para la instalacion
    <pre>./configure --enable-optimizations</pre>
    
    4. Instalar python y remplazarlo con el actual
    <pre>sudo make install</pre>


Ahora instalamos postgres y sus dependencias, copiemos y peguemos las siguientes lineas individualmente en la consola
<pre>sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update

sudo apt-get -y install postgresql</pre>


Ahora crearemos la tabla requerida en la base datos
<pre>sudo su postgres
psql
CREATE USER campanariosudo with password 'chaleco2022';
CREATE DATABASE campanariodb with owner campanariosudo;
\q
</pre>


Instalamos dependencias requeridas para los paquetes de python

<pre>sudo apt-get install libpq-dev python-dev
sudo apt install zlib1g-dev libjpeg-dev libpng-dev
python3 -m pip install --upgrade setuptools wheel ez_setup psycopg2
pip install --upgrade setuptools wheel ez_setup psycopg2</pre>

Una vez instalado todo, clonaremos el código de la página web y lo pondremos donde queramos. Puedes usar el siguiente comando:
<code><pre>wget <https://github.com/Heredento/campanario-chaleco.git></code></pre>

Esto descargará todos los archivos en el *directorio actual* que te encuentres, utiliza `cd campanario_chaleco` para entrar al directorio desde la terminal.

Crearemos un entorno virtual que se usará para instalar las dependencias (asegurate que la Raspberry esté conectada a internet) escribiendo el siguiente código:
<pre>python3 -m env venv</pre>
Esto se tardará un poco.
Después escribiremos:
<pre>source env/bin/activate</pre>
Eso hará que en tu terminal, al principio aparezca **(env)**

Ahora escribe el siguiente comando:
<pre>pip install -r requirements.txt</pre>
Esto instalará los paquetes necesarios para que tu no los instales manualmente uno por uno.

Ahora ubicamos el siguiente archivo `campanario/campanario/urls.py`
y editamos donde diga `path('', include('paginaweb.urls')),` agregando al principio un `#` que lo comenta
También editamos como `#handler404 = 'paginaweb.views.error_404_view'` y lo guardamos con CTRL+S y salimos con CTRL+X
En el archivo server_run.py, casi al final de archivo comentamos Server.lightState.run() para que quede como `#Server.lightState.run()`

Ahora corremos el migramos los datos como `python3 campanario/manage.py makemigrations`, y luego `python3 campanario/manage.py migrate`, esperamos un poco, y cuando mencione que se han creado unos modelos descomentamos las líneas `path('', include('paginaweb.urls')),` y `#handler404 = 'paginaweb.views.error_404_view'` de el archivo `campanario/campanario/urls.py` y corremos el código `python3 server_run.py` esto haría que la terminal muestre el estado de la página web.

En breve este muestra una dirección que suele terminar con `-:8080` esta la abrimos en el navegador y nos redirige a la página web, creamos nuestra cuenta (los datos deben ser reales por la verificación de email).
Ingresamos en el apartado de configuración y agregamos una configuración en la parte de "Encendido de agujas", una vez guardado, volvemos al terminal presionamos CTRL + C tres veces para cerrar el servidor y finalmente descomentamos el archivo server_run.py para que quede cómo `Server.lightState.run()`

Escribe `pwd` y retornarnará cómo algo cómo el mensaje siguiente: `home/usuario/el/directorio/que/elegiste`, copia ese resultado, guardalo y escribe `cd`, luego volveras a tu *directorio root*, ahora escribe <pre>touch start_server.sh</pre>esto creará un archivo **bash** que se usará para empezar el server cada vez que se reinicie.

Ese archivo lo editaras con el siguiente contenido y el mensaje que copiaste anteriormente.
<code><pre>
cd /home/campanario/campanario/campanario_chaleco
source env/bin/activate
python3 server_run.py
</pre></code>
Una vez guardado el archivo, escribe `pwd`, esto te retornará `/home/usuario` el cual le agregaremos
`@reboot bash` y `start_server.sh` al final el cual debería verse como:
<pre>@reboot bash /home/usuario/start_server.sh</pre>
Copiamos ese código, y escribimos `crontab -e`, posiblemente te pregunte si quieres usar un editor cómo vi, emacs, nano. Tú elige nano, usualmente escribiendo 1 y presionado ENTER.

Ahora estas ubicado dentro del archivo crontab el cual usa las fechas de los lados del teclado y ve hasta abajo justo una línea antes del texto `exit 0`(si no aparece no hay problema), ahora, pegamos el código pegado (usualmente presionando CTRL+SHIFT+V) `@reboot bash /home/usuario/start_server.sh` y lo guardamos presionando CTRL+S, ahora presionamos CTLR+Q y eso haría que te salgas del interfaz.

Una vez realizado esto, la Raspberry está lista para funcionar. La puede reiniciar, e incluso desconectar y volver a conectar.
