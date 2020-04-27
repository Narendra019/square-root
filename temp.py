# # # -*- coding: utf-8 -*-
# # """
# # Spyder Editor

# # This is a temporary script file.
# # # """
# # import matplotlib.pyplot as plt
# # import pandas as pd
# # import numpy as np
# # import xlrd
# # df=pd.read_excel("Book1.xlsx",index_col=0)
# # print(df.head())
# # print(df)
# # print(df.shape)
# # x=np.arange(1,20,1)
# # plt.bar(x, 10, 1)
# # print(df[0:18])
# # plt.xlabel('age')
# # plt.ylabel('value')
# # plt.xticks(x, "value", fontsize=6, rotation=30)
# # plt.show()
# # from __future__ import print_function



# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# TWOPI = 2*np.pi

# fig, ax = plt.subplots()

# t = np.arange(0.0, TWOPI, 0.001)
# s = np.sin(t)
# l = plt.plot(t, s)


# ax = plt.axis([0,TWOPI,-1,1])

# blueDot, = plt.plot([0], [np.sin(0)],'ro')

# def animate(i):
#     blueDot.set_data(i, np.sin(i))
#     print(i)
#     return blueDot,

# # create animation using the animate() function
# myAnimation = animation.FuncAnimation(fig, animate, frames=np.arange(0.0, TWOPI, 0.1), \
#                                       interval=100, blit=True, repeat=True)

# plt.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:59:40 2020

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial as sr
import string 

data=np.array([])

    
fig,ax= plt.subplots()   
sr =sr.Serial()
sr.port = 'COM3' #Arduino serial port
sr.baudrate = 2000000
sr.timeout = 10 #specify timeout when using readline()
sr.open()
# sr.reset_input_buffer()

plt.xlim(0,100)
plt.ylim(0,5)
plt.xlabel("p value",size=10,color="red")
plt.ylabel("q value",size=10,color="blue")  
 # ax.set_xdata(np.arange(0,len(data)))
 # ax.set_ydata(data)

def update(i):
     if sr.is_open==True:
       a=sr.readline()
       a.decode()
     global data
     # try:
            # if(len(data) < 100):
     data = np.append(data,float(a[0:7]))
     print(data)
     x=np.arange(0,len(data))
     plt.plot(x,data)
     
    
     #        else:
     #            data[0:99] = data[1:100]
     #            data[99] = float(a[0:4])
     # except ValueError:
     #         print(a)   
     #         pass
      


myAnimation= animation.FuncAnimation(fig, update,blit=False)
plt.show()     

# redDot,=ax.plot([x],[data])
# plt.title("SQUARE ROOT: " ,size=35)
# def animate(i):
#     redDot.set_data(i,i)
#     return redDot,
# myAnimation= animation.FuncAnimation(fig, animate,frames=len(x),interval=200,blit=True,repeat=True)
# plt.show()
