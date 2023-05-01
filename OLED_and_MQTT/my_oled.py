from machine import Pin, SoftI2C
import ssd1306
import gfx
from time import sleep
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
graphics = gfx.GFX(oled_width, oled_height, oled.pixel)
def F_data(msg):
    oled.fill_rect(105, 9, 9, 8, 0)
    oled.text(str('F'), 105, 9)
    oled.show()
def C_data(msg):
    oled.fill_rect(105, 9, 9, 8, 0)
    oled.text(str('C'), 105, 9)
    oled.show()
def rect_data(msg):
    #Clear OLED and set ii to 0
    oled.fill(0)
    ii = 0
    #Setting up the OLED
    oled.text(str('TEMP'), 0, 9)
    oled.text(str('WIND'), 0, 38)
    oled.text(str('0'), 35, 0)
    oled.text(str('C'), 105, 9)
    oled.text(str('0'), 35, 29)
    oled.text(str('M/S'), 105, 38)
    oled.rect(35, 9, 65, 8, 1)
    oled.rect(35, 38, 65, 8, 1)
    #Reading the Variables
    my_string = msg.decode('utf-8')
    my_values = [float(x) for x in my_string.split(';')]
    #Functions that act upon the given values
    if len(my_values) >= 7:
        for item in my_values:
            wind = my_values[2]
            windCo = my_values[3]
            temp = my_values[0]
            tempCo = my_values[1]
            currentCounter = my_values[4]
            thresholdCutoff = my_values[5]
            clock = my_values[6]   
        oled.text(str(int(tempCo)), 85, 1)
        oled.text(str(windCo), 77, 29)
        tempGauge = int(temp)/int(tempCo)
        windGauge = wind/windCo
        if tempGauge > 1:
            tempGauge = 1
        if windGauge > 1:
            windGauge = 1    
        oled.text(str(int(currentCounter)), 1, 56)
        oled.text(str('/'), 16, 56)
        oled.text(str(int(thresholdCutoff)), 24, 56)
        oled.fill_rect(35, 9, int(tempGauge*65.0), 8, 1)
        oled.fill_rect(35, 38, int(windGauge*65.0), 8, 1)
        oled.text(str(int(temp)), int((tempGauge*65.0)+28), 19)
        oled.text(str(wind), int((windGauge*65.0)+23), 48)
        oled.text(str(clock), 80, 56)
        print(type(msg))
    def F_data(msg):
        oled.fill_rect(105, 9, 9, 8, 0)
        oled.text(str('F'), 105, 9)
        oled.show()
    def C_data(msg):
        oled.fill_rect(105, 9, 9, 8, 0)
        oled.text(str('C'), 105, 9)
        oled.show()
    #Show everything on the OLED
    oled.show()