

import sqlite3
import tkinter  as tk 
from tkinter import * 
import time
import numpy as np

import os
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()



#------------------------------------------------------

root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Person Identification Using Face Detection & Machine Learning")
#------------------Frame----------------------



#-------function------------------------

def reg():
    
##### tkinter window ######
    
    print("reg")
    from subprocess import call
    call(["python", "user_registration.py"])   



def login():
    
##### tkinter window ######
    
    print("log")
    from subprocess import call
    call(["python", "user_login.py"])   
    


#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('r1.jpeg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Person Identification Using Face Detection", font=('times', 40,' bold '), height=1, width=40,bg="green",fg="white")
lbl.place(x=150, y=5)

framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=500, height=250, bd=5, font=('times', 14, ' bold '),bg="pink")
framed.grid(row=0, column=0, sticky='nw')
framed.place(x=450, y=300)
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(framed, text='Login Now',width=20,height=3,bg='dark blue',fg='white',command=login,font='bold').place(x=20,y=35)
button1 = tk.Button(framed, text='Register',width=20,height=3,bg='dark blue',fg='white',command=reg,font='bold').place(x=250,y=35)


root.mainloop()