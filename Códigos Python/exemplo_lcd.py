import lcd
import image
import time

#Usando string
lcd.init()
lcd.draw_string(50, 100, "Ola Mundo eu sou uma string!", lcd.RED, lcd.BLACK) #Primeiros dois argumentos sao a posicao do texto,
                                                                             #os outros dois sao a cor das letras e o fundo
time.sleep_ms(1000)

#Criando uma imagem

img = image.Image()
img.draw_string(25, 150, "Ola mundo eu sou uma imagem!", scale=2)
lcd.display(img)
