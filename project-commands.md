

> Currently learning git, github, django and more.
> This markdown file is just for note taking
 
### Start project
*Run django server: campanario*
    `python3 campanario/manage.py runserver 8080`

### Virtual environment
*Activate virtual environment*
    `source campanariovenv/bin/activate`

*Leave virtual environment*
    `deactivate`

### Pipreqs
*Generate requirements.txt for packages*
    `pipreqs --force`
    --force to overwrite file

*Install python packages*
    `pip install -r requirements.txt`


- python3 -m django startproject webTemplate
- python3 -m django startapp userform
- python3 manage.py runserver

### Posgrest commands

*Connect to campanariodb as campanariosudo*
    `psql -U campanariosudo -h 127.0.0.1 campanariodb`

*Check all tables django*
    `\dt;`


Accesar base de datos
    sudo su postgres
    psql

Comandos postgresql
    service postgresql

Contraseña superusuario postgres
    20160176

Conectar a base de datos
    \c camapanariodb;

Crear usuario 
    CREATE USER campanario WITH PASSWORD 'PASSWORD';

Info usuario DB 
    name: campanariosudo
    contraseña: 20160176

Checkear usuarios 
    \du

Poner roles para usuarios db 
    ALTER USER nombreusuario WITH SUPERUSER;

Borrar usuario 
    DROP USER nombreusuario;

Detener base de datos
    service  postgresql stop

Cambiar de usuario en linux 
    su <option> <user>

Dejar la base de datos 
    \q

Revisar las bases de datos 
    \l

Crear base de datos 
    CREATE DATABASE nombrebase;

create table amigos.test(firstname CHAR(15), lastname CHAR(20));
select * from amigos.text;
\d amigos.test; >>> Describe la base de datos
insert into amigos.test values('Carlos', 'López')

psql -U tu_usuario -h 127.0.0.1 tu_base_de_datos

psql -U campanariosudo -h 127.0.0.1 campanariodb


select * from userform_usuarioform;
20160176