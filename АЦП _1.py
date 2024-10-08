import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
troyka=13
comp=24

GPIO.setup(dac+[13], GPIO.OUT)

#GPIO.setup(troyka,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, 1)


def Binary(a):
    B=[int(x) for x in bin(a)[2:].zfill(8)]
    return B
'''    B = [int(x) for x in bin(a)[2:]]
    if len(B) < 8:
        t = 8-len(B)
        for i in range(t):
            B.insert(0, 0)'''
def ret(n):
    num=Binary(n)
    GPIO.output(dac, num)
    return (n*3.3/256)
try:
    while True:
        for x in range(256):
            ret(x)
            time.sleep(0.01)
            #print(GPIO.input(comp))
            if GPIO.input(comp):
                print(x/256*3.3)
                break
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()

