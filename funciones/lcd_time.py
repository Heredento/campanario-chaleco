import threading
import time , sys, os, drivers, RPi.GPIO as GPIO
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import Image, ImageFont, ImageDraw
from time import sleep
import socket
sys.path.append(os.getcwd())



time_folder = os.path.join(os.getcwd(), 'funciones/', 'clocktime/')
hour_file = os.path.join(time_folder, 'hour.txt')
min_file = os.path.join(time_folder, 'minute.txt')

static = os.path.join(os.getcwd(), 'funciones/', 'media/')
timefile = os.path.join(os.getcwd(),'funciones/','clocktime/', 'time.txt')

try:
    device = ssd1306(i2c(port=1, address=0x3C), width=128, height=64, rotate=0)
    device.contrast(10)
    ssdfound = True
    print('[ÉXITO] SSD1306 encontrado')
except Exception:
    ssdfound = False
    print('[ERROR] SSD1306 no encontrado')

try:
    lcd = drivers.Lcd()
    customimage = os.path.join(static, 'shinobu.png')
    logo = Image.open(customimage)
    logo.thumbnail((128, 64), Image.Resampling.BICUBIC)
    lcd_found = True
    print('[ÉXITO] LCD_I2C encontrado')
except Exception:
    lcd_found = False
    print('[ERROR] LCD_I2C no encontrado')
    
def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
        
    return ip    
    
def leer_hora():
    try: 
        with open(min_file, 'r') as m:
            m.flush()
            minuto = int(m.read())
        m.close()
        with open(hour_file, 'r') as h:
            h.flush()
            hora = int(h.read())
        h.close()
    
    
        hora_ = f'0{hora}' if hora <= 9 else hora
        minuto_ = f'0{minuto}' if minuto <= 9 else minuto
        tiempo = f'{hora_}:{minuto_}'

        return tiempo
    except Exception:
        return True    
    

saved_time = ""
while True:
    timetext=leer_hora()
    if timetext is True:
        continue

    try:
        if ssdfound is False:
            try:
                device = ssd1306(i2c(port=1, address=0x3C), width=128, height=64, rotate=0)
                device.contrast(10)
                ssdfound = True
                print('[ÉXITO] SSD1306 encontrado')
            except Exception:
                ssdfound = False


        if lcd_found is False:
            try:
                lcd = drivers.Lcd()
                customimage = os.path.join(static, 'shinobu.png')
                logo = Image.open(customimage)
                logo.thumbnail((128, 64), Image.Resampling.BICUBIC)
                lcd_found = True
                print('[ÉXITO] LCD_I2C encontrado')
            except Exception:
                lcd_found = False
                

   
        
        
        if saved_time != timetext:
                saved_time = timetext
                print(f"Hora guardada: {timetext} ")
        

        if ssdfound is True:
            with canvas(device, dither=True) as draw:
                customfont = os.path.join(static, 'VerminVibes1989.ttf')
                font = ImageFont.truetype(os.path.join(customfont), 30)
                fontip = ImageFont.truetype(os.path.join(customfont), 10)
                
                draw.bitmap((0, 0), logo)
                draw.text((55, 25), timetext, font=font)
                draw.text((70, 55), get_ip(), font=fontip)
            
        if lcd_found is True:
            lcd.lcd_backlight(10)  
            lcd.lcd_display_string("  HORA CHALECO", 1)
            lcd.lcd_display_string(f'      {timetext}', 2)
            
        sleep(1)
    except Exception as ex:
        print(f"{os.path.basename(__file__)}\nEX: {ex}")