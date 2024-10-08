import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
troyka=13
comp=24

GPIO.setup(dac+[13], GPIO.OUT)

GPIO.setup(troyka,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def Binary(a):
    B=[int(x) for x in bin(a)[2:].zfill(8)]
    return B
def NeBinary(B):
    k=0
    for x in range(8):
        k+=B[x]*(2**x)
    return k 
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
        x = [0 for i in range(8)]
        for i in range(0, 8):
            x[i] = 1 
            GPIO.output(dac, x)
            time.sleep(0.1)
            if GPIO.input(comp):
                x[i] = 0
                continue
            else:
                x[i] = 1
        print(NeBinary(x[::-1]))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
