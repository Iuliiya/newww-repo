import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
leds=[9, 10, 22, 27, 17, 4, 3, 2]
troyka=13
comp=24
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac+[13], GPIO.OUT)
B=[]

GPIO.setup(troyka,GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
'''!!!
!!! КОГДА на экране будет 207, то нажать на кнопку схемы

запускать программу, держа провод около компаратора
'''

def Binary(a): # число в двоичный код
    B=[int(x) for x in bin(a)[2:].zfill(8)]
    return B
def NeBinary(B): # двоичный код в число
    k=0
    for x in range(8):
        k+=B[x]*(2**x)
    return k 
def ret(n):
    num=Binary(n)
    GPIO.output(dac, num)
    return (n*3.3/256)
try:
    t1=time.time()
    while True:
        x = [0 for i in range(8)]
        for i in range(0, 8):
            x[i] = 1 
            GPIO.output(dac, x)
            time.sleep(0.005)
            if GPIO.input(comp):
                x[i] = 0
                continue
            else:
                x[i] = 1
        k=NeBinary(x[::-1])
        print(k)
        B.append(k)
        V=[0 for t in range(8)]
        for x in range(0,int(k/32)+1):
            V[x]=1
        if (k==0):
            GPIO.output(troyka, 0)
            t2=time.time()
            print(B)
            break
        GPIO.output(leds, V)
finally:
    t=(t2-t1)/len(B)
    with open("Вольт-временная_хар7_1.txt", "w") as F:
        F.write("\n".join([f"t={t}"]+[str(x) for x in B]))
    plt.plot(B)
    plt.show()
    GPIO.output(dac, 0)
    GPIO.cleanup()