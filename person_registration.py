
import sqlite3
import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms

from PIL import Image, ImageTk
import re
import random
from tkinter.filedialog import askopenfilename
import os
import cv2


window = tk.Tk()
window.geometry("700x600")
window.title("REGISTRATION FORM")
window.configure(background="grey")
global file
Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
photo=tk.StringVar()
#file=tk.StringVar()
file1=tk.StringVar()





def show():
    global file
    file = askopenfilename(initialdir=r'F:\criminal_identification_video\profile images', title='Select Image',
                                       filetypes=[("all files", "*.*")])
    
    image3 =Image.open(file)
    image3 =image3.resize((450,280), Image.ANTIALIAS)
    print(file)
    return file


def convertToBinaryData(filename):             #We have to add image to database thats why use this function to convert image into binary format
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB():
    global file
    fname = Fullname.get()
    addr = address.get()
    #un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    photo1 = file
    #Photo = convertToBinaryData(photo1)
    print(photo1)
    
    try:
        sqliteConnection = sqlite3.connect('evaluation.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO registration
                                  (Fullname, address, Email, Phoneno, Gender, age , photo) 
                                  VALUES (?,?,?,?,?,?,?)"""

        empPhoto = convertToBinaryData(photo1)
        #resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (fname, addr,email,mobile,gender,time,empPhoto)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
    ms.showinfo("Person Record","Person Registration Completed !!")
    window.destroy()

    from subprocess import call
    call(['python','person_identify.py'])

#insertBLOB(1, "Smith", "E:/Number_plate_recognization/profile images/1.jpg")
#insertBLOB(2, "David", "E:/Number_plate_recognization/profile images/2.jpg")
image2 = Image.open('bg1.jpg')
image2 = image2.resize((700, 700), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(window, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

l1 = tk.Label(window, text="Registration Form", font=("Times new roman", 30, "bold"), bg="#192841", fg="white")
l1.place(x=190, y=50)

# that is for label1 registration

l2 = tk.Label(window, text="Full Name :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l2.place(x=130, y=150)
t1 = tk.Entry(window, textvar=Fullname, width=20, font=('', 15))
t1.place(x=330, y=150)
# that is for label 2 (full name)


l3 = tk.Label(window, text="Address :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l3.place(x=130, y=200)
t2 = tk.Entry(window, textvar=address, width=20, font=('', 15))
t2.place(x=330, y=200)
# that is for label 3(address)


# that is for label 4(blood group)

l5 = tk.Label(window, text="E-mail :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l5.place(x=130, y=250)
t4 = tk.Entry(window, textvar=Email, width=20, font=('', 15))
t4.place(x=330, y=250)
# that is for email address

l6 = tk.Label(window, text="Phone number :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l6.place(x=130, y=300)
t5 = tk.Entry(window, textvar=Phoneno, width=20, font=('', 15))
t5.place(x=330, y=300)
# phone number
l7 = tk.Label(window, text="Gender :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l7.place(x=130, y=350)
# gender
tk.Radiobutton(window, text="Male", padx=5, width=5, bg="snow", font=("bold", 15), variable=var, value=1).place(x=330,
                                                                                                                y=350)
tk.Radiobutton(window, text="Female", padx=20, width=4, bg="snow", font=("bold", 15), variable=var, value=2).place(
    x=440, y=350)

l8 = tk.Label(window, text="Age :", width=12, font=("Times new roman", 15, "bold"), bg="snow")
l8.place(x=130, y=400)
t6 = tk.Entry(window, textvar=age, width=20, font=('', 15))
t6.place(x=330, y=400)

l4 = tk.Button(window, text="Upload Photo :", width=12, font=("Times new roman", 15, "bold"), bg="snow",command=show)
l4.place(x=130, y=450)



btn = tk.Button(window, text="Register", bg="#192841",font=("",20),fg="white", width=9, height=1, command=insertBLOB)
btn.place(x=260, y=500)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
window.mainloop()