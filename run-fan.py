#!/usr/bin/env python

importos
import time
importRPi.GPIO as GPIO

GPIO.setwarnings(False)
pin = 21 # The pin ID, edit here to change it
maxTMP = 40 # The high temperature in Celsius which will trigger the fan on
minTMP = 35 # The low temperature in Celsius which will trigger fan off

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
GPIO.setwarnings(False)

defgetCPUtemperature():
res = os.popen('vcgencmdmeasure_temp').readline()
temp =(res.replace("temp=","").replace("'C\n",""))
    #print(temp)
return temp

defgetTEMP():
CPU_temp = float(getCPUtemperature())
ifCPU_temp>maxTMP:
GPIO.output(pin, True)
elifCPU_temp<minTMP:
GPIO.output(pin, False)
return()

try:
while True:
getTEMP()
time.sleep(5) # Read the temperature every 5 sec, increase or decrease this limit if you want
exceptKeyboardInterrupt: # trap a CTRL+C keyboard interrupt 
GPIO.cleanup() # resets all GPIO ports used by this program
