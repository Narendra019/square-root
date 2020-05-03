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
data1=np.array([])
data2=np.array([])
fig,(ax1,ax2)= plt.subplots(2)  
plt.xkcd()
plt.style.use('ggplot')
ax1,ax2.set_ylim(0,1)

ax2.set_xlabel("SAMPLES",size=15,color="orange",fontname='Comic Sans MS')
ax1.set_ylabel("COUNTS",size=15,color="blue",fontname='Comic Sans MS')
ax2.set_ylabel("COUNTS",size=15,color="orange",fontname='Comic Sans MS')
ax1.grid(True)
ax2.grid(True)
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
           a= a.decode()
           print(a)
           print(a[0])
     global data1,data2
     ctd=0
     try:
            # if(len(data) < 100):
         data1 = np.append(data1,int(a[0]))
         print(data1)
         data2=np.append(data2,int(a[1]))
         print(data2)
         x=np.arange(0,len(data1))
         # t=np.arange(0,2*np.pi,0.1)

         # print(len(data1))
         ax1.plot(x,data2,"green",label="A Phase")
         ax2.plot(x,data1,"red",label="B Phase")
         freq = CountFrequency(data1) 
         # print(freq)
         plt.gcf()
         
         ax1.set_title("ROTARY ENCODER",color="red",fontname='Comic Sans MS',size=15)
         red_patch = mpatches.Patch(color='green', label='A phase:'+str(len(data1)))
         ax1.legend(handles=[red_patch],loc='upper right')
         Blue_patch = mpatches.Patch(color='blue', label='B phase:'+str(len(data1)))
         ax2.legend(handles=[Blue_patch],loc='upper right')
         ax1,ax2.set_xlim(0,len(data1))
               
     except ValueError:
              sr.close()
              sys.exit()

myAnimation= animation.FuncAnimation(fig, animate,blit=False,repeat=False)
plt.show()
         