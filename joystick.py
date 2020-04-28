# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:23:22 2020

@author: user
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial as sr
import string ,sys
import mouse, time
import pyautogui as py
sr =sr.Serial()
sr.port = 'COM4' #Arduino serial port
sr.baudrate=9600;
sr.timeout = 10 #specify timeout when using readline()
sr.open()
# py.moveTo(0, 756,duration=0.3886999)
while(True):
    
      try:
        if sr.is_open==True:
            a=sr.readline()
            a = ((a.decode()).strip()).split(',')
            data=np.array([])
            x = int(a[0])-521
            y = int(a[1])-526
            s = int(a[2])
            # if x==521 & y==526:
            #     mouse.move(0,0,absolute=True,duration=0.3887)
            #     exit
            print(x,y)
            cur_pos = mouse.get_position()
            new_x=cur_pos[0]
            new_y= cur_pos[1]
            x_new=x
            y_new=y
            print(x_new,y_new)
            py.moveRel(x_new,y_new,duration=0.25)
            if s==0:
                py.click(x_new,y_new,button='Right')
            # events = mouse.record()
            # print(events)
      except KeyboardInterrupt:
              sr.close()
              sys.exit()