import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.IN)
time.sleep(2.5)
while True:
        if GPIO.input(7) == True:
                print ("Parents detected!")
                x = raw_input("Is it True? \n")
                if x.lower() == "yes" :
                        GPIO.cleanup()
                        break
                elif x.lower() == "no" :
                        GPIO.cleanup()
                        time.sleep(2)
                        GPIO.setmode(GPIO.BOARD)
                        GPIO.setwarnings(False)
                        time.sleep(3)
