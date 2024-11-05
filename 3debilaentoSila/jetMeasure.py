import jetFunctions as j
from time import sleep
import RPi.GPIO as GPIO

directionPin = 27
enablePin = 22
stepPin = 17
Measure=[]
GPIO.setmode(GPIO.BCM)
GPIO.setup([directionPin, enablePin, stepPin], GPIO.OUT)
r=input("Введите расстояние от нуля: ")
n=int(input('Введите кол-во шагов: '))

def step():
    GPIO.output(stepPin, 0)
    sleep(0.005)
    GPIO.output(stepPin, 1)
    sleep(0.005)

for x in range(n):
    j.initSpiAdc()
    Measure.append(j.getAdc())
    print(j.getAdc())

    if n>0:
        GPIO.output(directionPin, 1)
        GPIO.output(enablePin, 1)
        step()
        GPIO.output(enablePin, 0)
    if n<0:
        GPIO.output(directionPin, 0)
        GPIO.output(enablePin, 1)
        step()
        GPIO.output(enablePin, 0)

    sleep(0.05)
    j.deinitSpiAdc()
with open(f'L{r}.txt', "w") as F:
    F.write("\n".join([str(x) for x in Measure]))

GPIO.output(directionPin, 0)
GPIO.output(enablePin, 1)
for i in range(n):
    step()
GPIO.output(enablePin, 0)