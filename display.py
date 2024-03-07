
import tkinter  as tk 
from tkinter import * 
import sqlite3
my_conn = sqlite3.connect('peson_detect.db')
###### end of connection ####

##### tkinter window ######
import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("400x400") 

r_set=my_conn.execute("SELECT * from user")
i=0 # row value inside the loop 
for student in r_set: 
    for j in range(len(student)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, student[j])
    i=i+1
    
my_w.mainloop()