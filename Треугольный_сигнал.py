import RPi.GPIO as GPIO
import time
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def dvoichni(a):
    B=[int(x) for x in bin(a)[2:]]
    if len(B)<8:
        t=8-len(B)
        for i in range(t):
            B.insert(0, 0)
    return B
try:
    while True:
        a=input('Введите число от 0 до 255: ')
        if not a.isdigit():
            a=input(f'не {a}, а число от 0 до 255:')
        a=int(a)
        num=dvoichni(a)
        s=int(input('Введите период всего сигнала (в секундах) ' ))
        s=s/256/2
        while True:
            for i in range(256):
                GPIO.output(dac, dvoichni(i))
                time.sleep(s)
            for i in range(255, -1, -1):
                GPIO.output(dac, dvoichni(i))
                time.sleep(s)
finally:
    GPIO.output(dac, 1)
    GPIO.cleanup()