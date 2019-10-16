import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

TRANSMIT_PIN = 21
pulse_delay = 0.0002655

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRANSMIT_PIN, GPIO.OUT)

adress_HT12E = '00000000'
data_out = '0000'
data_string = adress_HT12E + data_out
number_of_packages = 16


def datasend(number_of_packages, adress_HT12E, data_out):
	data_string = adress_HT12E + data_out
	for i in range(number_of_packages):
		GPIO.output(TRANSMIT_PIN, 1)
		time.sleep(pulse_delay)
		for t in (data_string): 
			GPIO.output(TRANSMIT_PIN, 0)
			if t == '0':
				time.sleep(pulse_delay*2)
			else:
				time.sleep(pulse_delay)
			GPIO.output(TRANSMIT_PIN, 1)
			if t == '0':
				time.sleep(pulse_delay)
			else:
				time.sleep(pulse_delay*2)
		GPIO.output(TRANSMIT_PIN, 0)
		time.sleep(pulse_delay*8) 

while True:
	datasend(number_of_packages, adress_HT12E, '0000' )
	#time.sleep(0.1)
	datasend(number_of_packages, adress_HT12E, '1000' )
	#time.sleep(0.1)
	datasend(number_of_packages, adress_HT12E, '1100' )
	#time.sleep(0.1)
	datasend(number_of_packages, adress_HT12E, '1110' )
	#time.sleep(0.1)
	datasend(number_of_packages, adress_HT12E, '0000' )
