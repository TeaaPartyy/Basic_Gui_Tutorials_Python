#made by Hamza Slaoui Habib
#basic program to create message box in python using tkinter
#message box to show to users
#beginners guide // functions not optimized
#this guide and the following others in the same file are inspired by the course offered by freecodechamp.org

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root = Tk() #creating the root
root.title("Basic Tutorial to create message boxes")
root.iconbitmap('c:/users/slaou/desktop/training/basic_gui_tutorials_python/myicons/pp.ico')
#define the path from where to get the icon, if the icon is not in the same folder as the program, you need to define the whole path
#NB: the icon should be an ico picture, which means should be a .ico
root.geometry("400x400") #deciding how big we want our initial window 


#these are different types of popup you can have:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

#functions to treat each type of messagebox
def infoBox():
    messagebox.showinfo("Hello World","This is an info Popup")
def warningBox():
    messagebox.showwarning("Hello World! ", "This is a Warning Popup")
def errorBox():
    messagebox.showerror("Hello World", "This is an Error Popup")
def questionBox():
        #myLabel1=Label(root,text=response).pack() => Use this to see the values given by "reponse" in order to understand the if loop
    response=messagebox.askquestion("Hello World?", "is this a Question Popup?")
        #1 stands for yes, 0 stands for no
    if response == "yes":
        messagebox.showinfo("Well, Hello there..","you are right! That was a question Popup")
    else:
        messagebox.showerror("Well Hello There..","That was a question Popup")
def cancelBox():
        #myLabel1=Label(root,text=response).pack() => Use this to see the values given by "reponse" in order to understand the if loop
        #1 stands for ok, 0 stands for cancel
    response=messagebox.askokcancel("Hello World?", "Do you want to cancel this okcancel Popup?")
    if response == 1:
        messagebox.showinfo("Well, Hello there..","This Popup will be canceled")
    else:
        messagebox.showwarning("Well Hello There..","you canceled the cancel :p")
def yesnoBox():
    response=messagebox.askyesno("Hello World?", "is this a yes/no Popup?")
            #myLabel1=Label(root,text=response).pack() => Use this to see the values given by "reponse" in order to understand the if loop
            #1 stands for yes, 0 stands for no
    if response == 1:
        messagebox.showinfo("Well, Hello there..","You are right ! That was a Yes/no Popup")
    else:
        messagebox.showerror("Well Hello There..","That was an Yes/no Popup")

#NB: showinfo, showerror, and showwarning all return "ok" as a response

#creating buttons for each type of info box
myButton1=Button(root, text="Info", command=infoBox).pack()
myButton2=Button(root,text="Warning", command=warningBox).pack()
myButton3=Button(root,text="Error", command=errorBox).pack()
mybutton4=Button(root,text="Question", command=questionBox).pack()
mybutton5=Button(root,text="Cancel",command=cancelBox).pack()
mubutton6=Button(root,text="YesNo",command=yesnoBox).pack()



mainloop() #as name says
