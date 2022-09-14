import requests

def check_connection():
    try:
        requests.head('https://www.google.com/', timeout=20)
        return True
    except Exception: 
        return False


while True:
    

    if check_connection()  is True:
        print("Conectado")
        # while True:
        #     if check_connection() is True:
        #         pass
        #     elif check_connection() is False:
        #         break
    elif check_connection()  is False:
        print("Desconectado")
        # while True:
        #     if check_connection() is False:
        #             pass
        #     elif check_connection() is True:
        #         break

    
