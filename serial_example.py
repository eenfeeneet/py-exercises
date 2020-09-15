from tkinter import*
#from shapely.geometry import polygon
import serial
import time



con_port = "/dev/ttyUSB0"
ser1 = serial.Serial(con_port,baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,
				bytesize=serial.EIGHTBITS)
print(ser1)
# en enable drive
ser1.write("en\r\n".encode("utf-8"))
# k disbale drive
#ser1.write("en\r\n".encode("utf-8"))

time.sleep(0.05)
# i acquiring the current current value
ser1.write("i\r\n".encode("utf-8"))
time.sleep(0.05)
out= ""

while ser1.inWaiting()>0:
	out += str(ser1.readline())
print(out.split('\n'))
ser1.close()