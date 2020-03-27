#!/usr/bin/env python

importRPi.GPIO as GPIO
importsubprocess

importos
os.system("sudosh -c 'echo 0 > /sys/class/leds/led1/brightness'") ##Use if pwr led needs to be switched off during start up
os.system("sudosh -c 'echo 0 > /sys/class/leds/led0/brightness'") ##Use if act led needs to be switched on during start up

GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(3, GPIO.FALLING)

subprocess.call(['shutdown', '-h', 'now'], shell=False)
