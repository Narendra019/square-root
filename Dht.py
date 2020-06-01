# -*- coding: utf-8 -*-
"""
Created on Mon May  4 22:18:53 2020

@author: Narendra Chowdary
"""
import tkinter as tk
import numpy as np
import serial as sr
from tkinter import ttk


# from tkinter import *
from colour import Color
import random
from time import strftime 
from PIL import ImageTk,Image

data1=np.array([])
data2=np.array([])
data3=np.array([])

#-----Main GUI code-----
root = tk.Tk()
root.title('Data ')
root.configure(background = 'light blue')
root.geometry('700x450') # set the window size
def time():
    string = strftime('%H:%M:%S %p') 
    t1.config(text = string) 
    t1.after(1000, time)
    print(string)

sr = sr.Serial('COM3',9600)
sr.reset_input_buffer()
path =r"C:\Users\Narendra Chowdary\Desktop\PPT\dht.jpg"
img= ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
t1=tk.Label(root,width=1,height=1,font=('calbiri',10,'bold'),bg="light blue",padx=30,pady=10)
t1.pack()
t1.place(relx = 0.06,rely = 0.03, anchor = 'center')


    
def update():
    frame0=tk.Frame(root,bg="skyblue")
    frame0.place(relwidth=0.69,relheight=0.3,relx=0.12,rely=0)  
    label7 =tk.Label(frame0,text="REALTIME MONITORING DHT HUMIDITY SENSOR & ENCODER", fg="black",bg="skyblue",font=('calbiri',10,'bold'),padx=10,pady=5).pack()  
    frame1=tk.Frame(root,bg="skyblue")
    frame1.place(relwidth=0.4,relheight=0.4,relx=0.02,rely=0.06)          
    label1 =tk.Label(frame1,text="Value", fg="black",bg="skyblue",font=('calbiri',10,'bold'),padx=10,pady=5).pack()
    frame2=tk.Frame(root,bg="sky blue")
    frame2.place(relwidth=0.4,relheight=0.4,relx=0.45,rely=0.06)          
    label2 =tk.Label(frame2,text="HUMIDITY", fg="black",bg="skyblue",font=('calbiri',10,'bold'),padx=10,pady=5).pack() 
    txt1=tk.Label(frame2,width=3,height=3,font=('calbiri',30),text=data3+str("H"),bg="skyblue").pack()
    frame3=tk.Frame(root,background="skyblue") 
    frame3.place(relwidth=0.4,relheight=0.4,relx=0.02,rely=0.45)
    label3 =tk.Label(frame3,text="TEMPERATURE", fg="black",bg="skyblue",font=('calbiri',10,'bold'),padx=10,pady=5).pack() 
    txt2=tk.Label(frame3,width=3,height=3,font=('calbiri',30),text=data2+str("C"),bg="skyblue").pack()
    frame4=tk.Frame(root,bg="sky blue")
    frame4.place(relwidth=0.4,relheight=0.4,relx=0.45,rely=0.45)
    label5 =tk.Label(frame4,text="ENCODER STATUS ", fg="black",bg="skyblue",font=('calbiri',10,'bold'),padx=10,pady=5).pack() 
    li=tk.Label(frame4,width=3,height=3,font=('calbiri',30),text=data1,bg="skyblue")
    li.pack()
    time()
    # labelset()
    root.after(1000,port)
    root.after(1000,update) 
    image1= tk.PhotoImage("C:\\Users\\Narendra Chowdary\\Desktop\download.PNG")
    label_for_image=tk.Label(root, image=image1)
    label_for_image.pack()
    root.mainloop()

       
def port():
   global data1,data2,data3
   
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
           
           
# add figure canvas
   except ValueError:
        sr.close()    
        
while(True):
     port()
   
     update()
     

