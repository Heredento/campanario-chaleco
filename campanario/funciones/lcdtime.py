import django
from django.conf import settings
from django.conf.urls.static import static
import time, sys, os
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import Image, ImageFont, ImageDraw
from django.conf import settings


fontfolder=os.path.join(settings.STATICFILES_DIRS, 'utilidad/', 'fonts/', 'lcddisplay/')
logofolder=os.path.join(settings.STATICFILES_DIRS, 'display/')

# NB ssd1306 devices are monochromatic; a pixel is enabled with
#    white and disabled with black.
# NB the ssd1306 class has no way of knowing the device resolution/size.
device = ssd1306(i2c(port=1, address=0x3C), width=128, height=64, rotate=0)

# set the contrast to minimum.
device.contrast(10)


# load the rpi logo.
logo = Image.open(os.path.join(logofolder, 'shinobu.png'))
logo.thumbnail((128, 64), Image.Resampling.BICUBIC)


# show some info.
print(f'Size: {device.size} |  Mode: {device.mode} | Logo size: {logo.size} | Logo mode {logo.mode}')

# NB this will only send the data to the display after this "with" block is complete.
# NB the draw variable is-a PIL.ImageDraw.Draw (https://pillow.readthedocs.io/en/3.1.x/reference/ImageDraw.html).
# see https://github.com/rm-hull/luma.core/blob/master/luma/core/render.py
# for i in range(60):
i = 20
with canvas(device, dither=True) as draw:

    font = ImageFont.truetype(os.path.join(fontfolder, 'VerminVibes1989.ttf'), 30)
    draw.bitmap((0, 0), logo)
    timetext=f'10:{i}'
    if i<=9:
        timetext=f'10:0{i}'
    draw.text((60, 25), timetext, font=font)
    time.sleep(1)

time.sleep(5*60)

