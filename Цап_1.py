import RPi.GPIO as GPIO
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
        a=input('Введите число от 0 до 255:')
        if (not (str(a).isdigit())) or int(a)<0: 
            a=input('Введите число от 0 до 255:')
        a=int(a)
        num=dvoichni(a)
        if (str(a).isdigit() and a%1==0 and 0<=a<=255):
            GPIO.output(dac, num)
            print(a/256*3.3)
except ValueError:
   print("Это не число" )
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()