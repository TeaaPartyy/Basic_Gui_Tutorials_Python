#made by Hamza Slaoui Habib
#basic program to create a new window in python using tkinter
#beginners guide // functions not optimized
#this guide and the following others in the same file are inspired by the course offered by freecodechamp.org

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk() #creating the root
root.title("Basic Tutorial to create a new window")
root.iconbitmap('c:/users/slaou/desktop/training/basic_gui_tutorials_python/myicons/pp.ico')
#define the path from where to get the icon, if the icon is not in the same folder as the program, you need to define the whole path
#NB: the icon should be an ico picture, which means should be a .ico
root.geometry("400x400") #deciding how big we want our initial window


def createWindow():
    topWindow = Toplevel() #the new window created
    myLabel1 = Label(topWindow, text="This is the new window").pack()
    closeButton= Button(topWindow,text="Close Window",command=topWindow.destroy).pack() #to close the window use the command .destroy
    #NB to use icons, create them as global variables


openButton=Button(root,text="\n \n Click on me to create a new window",command=createWindow).pack()

#You can put on it anything we created in the previous guides, the difference is where it will take form
#previously, all buttons, labels, frames...etc where under Root, if you want them to be under a new window, replace root by the name of the new window


mainloop() #as name says
