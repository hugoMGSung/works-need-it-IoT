# 푸시버튼 누르면 QR코드 읽는 예제
import RPi.GPIO as GPIO
import time
import webbrowser
import urllib.request

import cv2
from picamera2 import Picamera2

cam = Picamera2()
cam.preview_configuration.main.size=(800,600) 
cam.preview_configuration.main.format='RGB888'
cam.preview_configuration.align()

cam.configure('preview')
cam.start()

button = 24
count = 0

def clickHandler(channel):
    global count
    count = count + 1
    # print(count)
    frame = cam.capture_array()
    qr = cv2.QRCodeDetector()
    data, box, str_qrcode = qr.detectAndDecode(frame)
    url = str(data)
    print(url)
    res = urllib.request.urlopen(url)
    if (res.status == 200):
        webbrowser.open(url)

    cv2.imshow('piCam', frame)
    cv2.destroyAllWindows()


GPIO.setwarnings(False) # 쓸데없는 경고표시 로그 사라짐
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(button, GPIO.RISING, callback=clickHandler)

while (True):
    time.sleep(1)
