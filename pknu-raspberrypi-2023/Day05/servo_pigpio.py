import pigpio
import time

pwm_pin = 18
pi = pigpio.pi()

while True:
    pi.set_servo_pulsewidth(pwm_pin, 0)
    time.sleep(1)

    pi.set_servo_pulsewidth(pwm_pin, 500)
    time.sleep(1)

    pi.set_servo_pulsewidth(pwm_pin, 1500)
    time.sleep(1)

    pi.set_servo_pulsewidth(pwm_pin, 2500)
    time.sleep(1)
