# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:02:03 2020

@author: user
"""
import collections 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial as sr
import string ,sys
import datetime
import matplotlib.patches as mpatches
data=np.array([])
fig,ax= plt.subplots()  
plt.xkcd()
plt.style.use('ggplot')
plt.ylim(0,2)

plt.xlabel("SAMPLES",size=15,color="orange",fontname='Comic Sans MS')
plt.ylabel("COUNTS",size=15,color="blue",fontname='Comic Sans MS')
plt.grid(True)
sr =sr.Serial()
sr.port = 'COM4' #Arduino serial port
sr.baudrate=9600;
sr.timeout = 10 #specify timeout when using readline()
sr.open()
def CountFrequency(data): 
    return collections.Counter(data) 

def animate(i):
     if sr.is_open==True:
           a=sr.readline()
           a.decode()
           print(a)
     global data
     ctd=0
     try:
            # if(len(data) < 100):
         data = np.append(data,int(a))
         print(data)
         x=np.arange(0,len(data))
    
         print(len(data))
         plt.plot(x,data,"green",label="A Phase")
         freq = CountFrequency(data) 
         print(freq)
         plt.gcf()
         plt.title("PULSES",color="red",fontname='Comic Sans MS',size=15)
         red_patch = mpatches.Patch(color='green', label='A phase:'+str(len(data)))
         ax.legend(handles=[red_patch],loc='upper right')
         plt.xlim(0,len(data))
               
     except ValueError:
              sr.close()
              sys.exit()

myAnimation= animation.FuncAnimation(fig, animate,blit=False,repeat=False)
plt.show()
         