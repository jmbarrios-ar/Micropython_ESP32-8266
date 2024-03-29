import time
from umqtt.simple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()
import dht
from machine import Pin

ssid = '247IASbros2.4'
password = 'T3reKByo2023$'
mqtt_server = '192.168.24.150'
client_id = ubinascii.hexlify(machine.unique_id())
topic_pub = b'esp8266/DHT11'

ultimo_mensaje = 0
intervalo_mensajes = 10


station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Conexion exitosa')
print(station.ifconfig())

sensor = dht.DHT11(Pin(2))

def conectar_a_MQTT():
  global client_id, mqtt_server
  client = MQTTClient(client_id, mqtt_server)
  client.connect()
  print('Conectado a %s broker MQTT' % mqtt_server)
  return client

def reconectar():
  print('Fallo de conexion con broker MQTT. Reconectando...')
  time.sleep(10)
  machine.reset()

try:
  client = conectar_a_MQTT()
except OSError as e:
  reconectar()

while True:
  try:
    if (time.time() - ultimo_mensaje) > intervalo_mensajes:
      sensor.measure()
      temperatura = sensor.temperature()
      humedad = sensor.humidity()
      msg = (b'{0:3.1f},{1:3.1f}'.format(temperatura, humedad))
      client.publish(topic_pub, msg)
      ultimo_mensaje = time.time()
  except OSError as e:
    reconectar()
