import RPi.GPIO as GPIO
try:
    dac=[8, 11, 7, 1, 0, 5, 12, 6]
    #pinPWM=7
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(dac, GPIO.OUT, initial=GPIO.HIGH)
    pwm=GPIO.PWM(21, 1000)
    pwm.start(0)
    while True:
        w=int(input())
        pwm.ChangeDutyCycle(w)
finally:
    GPIO.output(21, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()