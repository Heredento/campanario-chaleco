import socket, sys, os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip = s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]

script = f'source env/bin/activate; python3 campanario/manage.py runserver {ip}:8080'
os.system(script)