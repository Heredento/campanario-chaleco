import os, sys, threading

pathfile=os.path.join(os.getcwd().replace('funciones', ''), 'campanario/', 'media/', 'songs/', 'song2.py')
with open(pathfile) as f:
    exec(compile(f.read(), 'song2', "exec"))
    # print(f.read())
print(pathfile)