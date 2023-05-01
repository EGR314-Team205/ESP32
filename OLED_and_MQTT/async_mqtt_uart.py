# Derived from: 
# * https://github.com/peterhinch/micropython-async/blob/master/v3/as_demos/auart.py
# * https://github.com/tve/mqboard/blob/master/mqtt_async/hello-world.py


from mqtt_async import MQTTClient, config
import uasyncio as asyncio
import time
from machine import UART
import my_oled
import logging
logging.basicConfig(level=logging.DEBUG)

MAXTX = 4

# Change the following configs to suit your environment
TOPIC_PUB = 'EGR314/Team205/DATA'
TOPIC_SUB1 = 'EGR314/Team205/DATA'
TOPIC_SUB2 = 'EGR314/Team205/THRESH'

config.server = 'egr3x4.ddns.net' # can also be a hostname
# config.ssid     = 'LEGO CHOUSE'
# config.wifi_pw  = '123456789ch'
config.ssid     = 'photon'
config.wifi_pw  = 'particle'

uart = UART(2, 9600,tx=17,rx=16)
uart.init(9600, bits=8, parity=None, stop=1,flow=0) # init with given parameters

async def receiver():
    b = b''
    sreader = asyncio.StreamReader(uart)
    while True:
        res = await sreader.read(1)
        if res==b'\r':
            await client.publish('EGR314/Team205/DATA'.encode(), b, qos=1)
            print('published', b)
            b = b''
        else:
            b+=res
def callback(topic, msg, retained, qos):
    print('callback',topic, msg, retained, qos)
    if topic == 'EGR314/Team205/DATA'.encode():
            my_oled.rect_data(msg)
    elif topic == 'EGR314/Team205/THRESH'.encode():
        if msg.decode() == "F":
            my_oled.F_data(msg)
        elif msg.decode() == "C":
            my_oled.C_data(msg)

async def conn_callback(client):
    await client.subscribe(TOPIC_SUB1, 1)
    await client.subscribe(TOPIC_SUB2, 1)
    

async def main(client):
    await client.connect()
    asyncio.create_task(receiver())
    while True:
        await asyncio.sleep(1)
config.subs_cb = callback
config.connect_coro = conn_callback
client = MQTTClient(config)
loop = asyncio.get_event_loop()
loop.run_until_complete(main(client))