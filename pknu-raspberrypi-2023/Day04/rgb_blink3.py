# LED RGB 깜빡이기
import RPi.GPIO as GPIO
import time

red = 17; green = 22; blue = 27 # Ground 역할(green, blue가 반대로 연결되어 있음)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(red, True)
GPIO.output(green, True)
GPIO.output(blue, True) # 여기까지 초기화

try:
    while True:
        # RED+GREEN = yellow / RED+BLUE = pink / GREEN+BLUE = sky
        # RED+GREEN+BLUE = white
        GPIO.output(red, False) # RED on
        GPIO.output(green, True)
        GPIO.output(blue, True)
        time.sleep(1)
        GPIO.output(red, True)
        GPIO.output(green, False) # GREEN on
        GPIO.output(blue, True)
        time.sleep(1)        
        GPIO.output(red, True)
        GPIO.output(green, True)
        GPIO.output(blue, GPIO.LOW) # BLUE on
        time.sleep(1)        

except KeyboardInterrupt:
    GPIO.output(red, GPIO.HIGH)
    GPIO.output(green, GPIO.HIGH)
    GPIO.output(blue, GPIO.HIGH)
    GPIO.cleanup()