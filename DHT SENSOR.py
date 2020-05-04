# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:25:48 2020

@author: user
"""
import tkinter as tk
import numpy as np
import serial as sr
from tkinter import ttk

#-----Main GUI code-----
root = tk.Tk()
root.title('Data ')
root.configure(background = 'light blue')
root.geometry('700x450') # set the window size
sr = sr.Serial('COM4',9600);
sr.reset_input_buffer()
# comboExample = ttk.Combobox(root, 
#                             values=[
#                                     "January", 
#                                     "February",
#                                     "March",
#                                     "April"])
# comboExample.pack()
# comboExample.current(1)

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
 frame1=tk.Frame(root,bg="blue")
 frame1.place(relwidth=0.4,relheight=0.4,relx=0.02,rely=0.05)          
 label1 =tk.Label(frame1,text="Value", fg="dark green",font=('calbiri'),padx=10,pady=5).pack()
 frame2=tk.Frame(root,bg="white")
 frame2.place(relwidth=0.4,relheight=0.4,relx=0.45,rely=0.05)          
 label2 =tk.Label(frame2,text="Value", fg="dark green",font=('calbiri'),padx=10,pady=5).pack() 
 frame3=tk.Frame(root,bg="yellow")
 frame3.place(relwidth=0.4,relheight=0.4,relx=0.02,rely=0.45)
 frame4=tk.Frame(root,bg="pink")
 frame4.place(relwidth=0.4,relheight=0.4,relx=0.45,rely=0.45)
 txt=tk.Label(frame4,width=3,height=3,font=('calbiri',10),text=data1,bg="pink").pack()
# add figure canvas
except ValueError:
        sr.close()
root.mainloop()
#  start = tk.Button(root, text = "Start", font = ('calbiri',12))
# # start.place(x = 100, y = 450 )
#  stop = tk.Button(root, text = "Stop", font = ('calbiri',12))
#  stop.place(x=50, y=500)
#----start serial port----



