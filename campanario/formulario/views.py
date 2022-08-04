from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from . import models #authfunctions, db
import bcrypt #https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/

## Paginas web inicial
def signin(request):
    template = loader.get_template('formulario/auth_login.html')
    contenido={
        'error': False,
        'registrado':True,
    }
    return HttpResponse(template.render(contenido, request))

def signup(request):
    template = loader.get_template('formulario/auth_register.html')
    contenido={
        'error': False
    }
    return HttpResponse(template.render(contenido, request))

def registrated(request):
    template = loader.get_template('formulario/auth_registrated.html')
    contenido={
        'verificado': False,
        'correo': ''
    }
    return HttpResponse(template.render(contenido, request))

def validate(request):
    template = loader.get_template('formulario/auth_validate.html')
    contenido={
        'verificado': False,
        'correo': ''
    }
    return HttpResponse(template.render(contenido, request))

def credits(request):
    template = loader.get_template('formulario/auth_credits.html')
    return HttpResponse(template.render(request))


## Funciones métodos POST y GET
"""
def register(request):
    # print(request.POST)
    
    if request.method == 'POST':
        usuario=''.join(request.POST['username'])
        correo=''.join(request.POST['usremail'])
        contraseña=''.join(request.POST['passwrd'])
        query = f"SELECT * FROM userform_usuarioform WHERE usr_name = '{usuario}' or usr_email='{correo}';"
        db.cur.execute(query)
        res = len(db.cur.fetchall())
        # print(res)
        if res > 0:
            template = loader.get_template('formulario/registro.html')
            contenido={
                'error': True
            }
            return HttpResponse(template.render(contenido, request))            

        elif res == 0:
            b = contraseña.encode('utf-8')
            hashed = bcrypt.hashpw(b, bcrypt.gensalt()) 

            registrar=models.usuarioform(
            usr_name=usuario,
            usr_email=correo,
            usr_password=hashed,
            auth_code=authfunctions.gencode(),
            auth_confirm=True
            )
            registrar.save()

            template = loader.get_template('formulario/verifymail.html')
            contenido={
                'verificado': True,
                'correo': correo
            }
            return HttpResponse(template.render(contenido, request))

            
            # return HttpResponseRedirect('/campanario/acceso/')

            
        # print("Cerrando base de datos")
        db.cur.connection.close()
    

    else:
        return redirect('/campanario/registro/')
    
def login(request):

    if request.method == 'POST':
        usuario=''.join(request.POST['username'])
        contraseña=''.join(request.POST['passwrd'])
        # hashing password
        
        #validate existence of such user
        queryvalidate = f"select * from userform_usuarioform where usr_name='{usuario}' or usr_email='{usuario}';"
        db.cur.execute(queryvalidate)
        res = len(db.cur.fetchall())


        if res > 0: #such user exists
            # print(f"{usuario} es existente")

            ubpass = contraseña.encode('utf-8')
            # db gets usr password
            querypass=f"select usr_password from userform_usuarioform where usr_name='{usuario}' or usr_email='{usuario}';"
            db.cur.execute(querypass)
            getpass = db.cur.fetchall()[0]

            dbpass = bytes(''.join(getpass)[2:-1], 'utf-8') #from list to a single string
            res = bcrypt.checkpw(ubpass, dbpass)
            # print(res)
            

        
            if res is True: #contraseña correcta
                queryauth = f"select auth_confirm from userform_usuarioform where usr_name='{usuario}' or usr_email='{usuario}';"
                db.cur.execute(queryauth)
                getauth = db.cur.fetchall()[0][0]
                # print(f"getauth: {getauth}: {type(getauth)} ")
                # print(f"queryauth: {queryauth}: {type(queryauth)} ")
                if getauth is True:
                    
                    template = loader.get_template('userform/acceso.html')
                    contenido= {
                    'registrado':False # Contraseña incorrecta
                    }
                    return HttpResponse(template.render(contenido, request))

                elif getauth is False:
                    return redirect('/campanario/eventos/')

            elif res is False:
                template = loader.get_template('userform/acceso.html')
                contenido= {
                'error':True # Contraseña incorrecta
                }
                return HttpResponse(template.render(contenido, request))


        else: #such user doesn't exist
            template = loader.get_template('userform/acceso.html')
            contenido= {
                'error':True # Usuario no existe
            }
            return HttpResponse(template.render(contenido, request))


    else:
        return redirect('/campanario/acceso/')

def registered():
    return redirect('/campanario/verificacion/')

def verify(request):
    # print(request.POST)
    correo="".join(request.POST['correo'])
    codigo="".join(request.POST['codigo'])
    # print(f"{correo}:{type(correo)} | {codigo}: {type(codigo)}")

    query = f"SELECT * FROM userform_usuarioform WHERE usr_email='{correo}' or usr_name='{correo}';"
    db.cur.execute(query)
    res = len(db.cur.fetchall())
    # print(res)

    match (res):
        case 0: # No existe usuario
            template = loader.get_template('userform/verify.html')
            contenido={
                'error': True,
                'exitoso': False
            }
            return HttpResponse(template.render(contenido, request))

        case 1: #Existe usuario
            queryauth = f"SELECT auth_code FROM userform_usuarioform WHERE usr_email='{correo}' or usr_name='{correo}';"
            db.cur.execute(queryauth)
            res = db.cur.fetchall()[0][0]
            # print(f"{res}:{type(res)}")


            if codigo == res:
                get=models.usuarioform.objects.get(usr_name=correo)
                get.auth_confirm=False
                get.save()


                template = loader.get_template('userform/verify.html')
                contenido={
                    'error': False,
                    'exitoso': True,
                    'errorAuth': False,
                    
                }
                return HttpResponse(template.render(contenido, request))

            else:
                template = loader.get_template('userform/verify.html')
                contenido={
                    'errorAuth': True,
                    'exitoso': False,
                    
                }
                return HttpResponse(template.render(contenido, request))


        case other:
            template = loader.get_template('userform/verify.html')
            contenido={
                'error': False
            }
            return HttpResponse(template.render(contenido, request))
"""