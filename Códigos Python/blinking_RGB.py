from fpioa_manager import fm #Mapeamento das GPIO
from Maix import GPIO #Classe GPIO
import time #Usado para fazer o delay entre os leds

#LED_G -> IO12
#LED_R -> IO13
#LED_B -> IO14

io_led_red = 13
io_led_green = 12
io_led_blue = 14

fm.register(io_led_red, fm.fpioa.GPIO0)
fm.register(io_led_green, fm.fpioa.GPIO1)
fm.register(io_led_blue, fm.fpioa.GPIO2)

led_r=GPIO(GPIO.GPIO0, GPIO.OUT)
led_g=GPIO(GPIO.GPIO1, GPIO.OUT)
led_b=GPIO(GPIO.GPIO2, GPIO.OUT)

while(1):
    led_r.value(0)
    time.sleep_ms(1000)
    led_r.value(1)
    led_g.value(0)
    time.sleep_ms(1000)
    led_g.value(1)
    led_b.value(0)
    time.sleep_ms(1000)
    led_b.value(1)

