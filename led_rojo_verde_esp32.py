#Este código crea dos objetos Pin para controlar los pines 2 y 4, que se conectan a los LED rojo y verde, respectivamente.
#Luego, en un bucle infinito, enciende y apaga cada LED por la cantidad de tiempo correspondiente usando la función time.sleep().
#El resultado será que el LED rojo parpadeará cada segundo y el LED verde parpadeará cada dos segundos.
from machine import Pin
import time

led_rojo = Pin(2, Pin.OUT)
led_verde = Pin(4, Pin.OUT)

while True:
    # Encender el LED rojo
    led_rojo.value(1)
    time.sleep(1)  # Esperar 1 segundo
    led_rojo.value(0)  # Apagar el LED rojo

    # Encender el LED verde
    led_verde.value(1)
    time.sleep(2)  # Esperar 2 segundos
    led_verde.value(0)  # Apagar el LED verde

