# Monocular camera

import sensor
import lcd

lcd.init()

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_brightness(2) # range [-2 ~ +2] para ambientes escuros usar 2
#sensor.set_auto_gain(1)
sensor.run(1)

while True:
    img = sensor.snapshot()
    lcd.display(img)
