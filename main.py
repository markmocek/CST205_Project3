import Tkinter
from Tkinter import *
import tkMessageBox
import tkFileDialog
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfile
import Tkconstants
import os


def displayText():
    """ Display the Entry text value. """
    global entryWidget


    if entryWidget.get().strip() == "":
         tkMessageBox.showerror("Tkinter Entry Widget", "Enter Secret Message")
    else:
         tkMessageBox.showinfo("Tkinter Entry Widget", "Secret Message =" + entryWidget.get().strip())
         f = open("Message.txt","w")
         f.write(entryWidget.get().strip()) 
         f.close()
         file = open("Message.txt","r")
         msg = file
         print file.read()

if __name__ == "__main__":     
   
    root = Tk()
 

a = Button(root, text="Open", command= openfile)
a.pack()

root.title("Tkinter Entry Widget")
root["padx"] = 40
root["pady"] = 20   
# Create a text frame to hold the text Label and the Entry widget
textFrame = Frame(root) 
#Create a Label in textFrame
entryLabel = Label(textFrame)
entryLabel["text"] = "Enter the text:"
entryLabel.pack(side=LEFT)

# Create an Entry Widget in textFrame
entryWidget = Entry(textFrame)
entryWidget["width"] = 50
entryWidget.pack(side=LEFT)
textFrame.pack()

button = Button(root, text="Submit", command=displayText)
button.pack()

root.mainloop()
