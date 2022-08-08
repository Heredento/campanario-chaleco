python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 campanario/manage.py makemigrations
python3 campanario/manage.py migrate