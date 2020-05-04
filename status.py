import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial as sr
import sys
sr =sr.Serial()
sr.port = 'COM4' #Arduino serial port
sr.baudrate=9600;
sr.timeout = 10 #specify timeout when using readline()
sr.open()
while(True):
 try:
   if sr.is_open==True:
           a=sr.readline()
           a= a.decode()
           print(a[:])
           data1=a[0]+a[1]
           data2=a[2]+a[3].strip()
           data3=a[4]+a[5]
           print("A phase:",data1)
           print("temperature:",data2)
           print("Humidity:",data3)
           # print("humidity",data4)
 except IndexError:
           sys.exit()
           sr.close()