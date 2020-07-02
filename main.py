import Adafruit_CharLCD as LCD
from datetime import datetime
import time

lcd_rs = 22
lcd_en = 26
lcd_d4 = 5
lcd_d5 = 6
lcd_d6 = 13
lcd_d7 = 19

# 16x2
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

while(1):
    current_dt = datetime.now()
    current_date = current_date.strftime('%m-%d')
    current_time = current_date.strftime('%H:%M:%S')
    lcd.clear()
    lcd.message(current_date ' ' + current_time)
    time.sleep(1)