#name   : Create GUI using Python Tkinter
#author : CodeMoe
#date   : 26 August ,2019

#initializing tkinter
from tkinter import *
import tkinter

###Introduction to GUI
##top = Tk()                    #initalizing top
##L1 = Label(top, text="HI")    #module label to print text 
##L1.pack(side = LEFT)          #pack is key to package everything in layout (left)
##E1 = Entry(top, bd =5)        #entry method to create blank entry (textbox)
##E1.pack(side = RIGHT)         #pack to right
##B=Button(top, text ="Hello",) #create button with Text
##B.pack()                      #Pack button
##top.mainloop()                #To keep everything possible until you close the GUI
####

def process():
    try:
        #INPUT
        number1=Entry.get(E1)
        number2=Entry.get(E2)
        operator=Entry.get(E3)
        #PROCESS
        number1=int(number1)
        number2=int(number2)
        if operator =="+":
            answer=number1+number2
        if operator =="-":
            answer=number1-number2
        if operator=="*":
            answer=number1*number2
        if operator=="/":
            answer=number1/number2
        Entry.clipboard_clear
        Entry.insert(E4,0,answer)
        #OUTPUT
        print(answer)
    except ValueError:
        tkMessageBox.showwarning("Warning","Please enter value in integer")



##Design GUI
top = Tk()
L1 = Label(top, text="My Calculator",).grid(row=0,column=1)
L2 = Label(top, text="Number 1",).grid(row=1,column=0)
L3 = Label(top, text="Number 2",).grid(row=2,column=0)
L4 = Label(top, text="Operator",).grid(row=3,column=0)
L4 = Label(top, text="Answer",).grid(row=4,column=0)
E1 = Entry(top, bd =3) #bd = border, set the thickness of entry box
E1.grid(row=1,column=1)
E2 = Entry(top, bd =3)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =3)
E3.grid(row=3,column=1)
E4 = Entry(top, bd =3)
E4.grid(row=4,column=1)
B=Button(top, text ="Submit",command = process).grid(row=5,column=1)
top.mainloop()





        
