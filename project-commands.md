

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


### Posgrest commands

*Connect to campanariodb as campanariosudo*
    `psql -U campanariosudo -h 127.0.0.1 campanariodb`

*Check all tables django*
    `\dt;`


