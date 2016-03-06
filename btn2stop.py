import time
import os
import RPi.GPIO as GPIO

PIN = 18
COUNT = 0
END = 6
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)

while True:
  if COUNT == END:
    COUNT = 0
    os.system("killall Pi3TVClock.py")
    print "Killed Pi3TVClock"
  if GPIO.input(PIN):
    COUNT += 1
  time.sleep(0.5)