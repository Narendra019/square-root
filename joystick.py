# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:37:34 2020

@author: Narendra Chowdary
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial as sr
import string ,sys
import mouse, time

sr =sr.Serial()
sr.port = 'COM3' #Arduino serial port
sr.baudrate=9600;
sr.timeout = 10 #specify timeout when using readline()
sr.open()
while(True):

 try:
   if sr.is_open==True:
       a=sr.readline()
       a = ((a.decode()).strip()).split(',')
       data=np.array([])
       x = int(a[0])+63
       y = int(a[1])-100 
       s = int(a[2])
       print(x,y)
       cur_pos = mouse.get_position()
       new_x=cur_pos[0]-521
       new_y= cur_pos[1]-526
       x_new =x
       y_new =y
       print(x_new,y_new)
       mouse.move(x_new, y_new)
  
 except KeyboardInterrupt:
         sr.close()
         sys.exit()