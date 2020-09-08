#made by Hamza Slaoui Habib
#basic program to create checkboxes in python using tkinter
#Program will show how to implement the checkboxes and show how to use them accordingly in different situations
#Part I shows the default checkboxes while Part II shows how to custome them
#this will complement the previous guides of radio buttons in order to cover all the basics in that sense
#beginners guide // functions not optimized
#this guide and the following others in the same file are inspired by the course offered by freecodechamp.org

from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


root = Tk() #creating the root
root.title("Basic Tutorial to create message boxes")
root.iconbitmap('c:/users/slaou/desktop/training/basic_gui_tutorials_python/myicons/pp.ico')
#define the path from where to get the icon, if the icon is not in the same folder as the program, you need to define the whole path
#NB: the icon should be an ico picture, which means should be a .ico
root.geometry("400x400") #deciding how big we want our initial window

#first part of the program is about the default values of the checkboxes, second part will be how to personalize them


#function to show the status of the default checkbox and the value it gets if it's either checked or not
def checkStatus():
    mylabel1 = Label(root, text=checkVar.get()).pack()
    #1 stands for checkbox checked / 0 stands for checkbox unchecked.
    #the 0 and 1 are the default values of the checkboxes
    #we can use this information accordingly in our programs for if statements, loops ...etc etc

#Function to show the status of the personalized checkbox and the values it gets if it's either checked or not
def customStatus():
    myLabel2= Label(root, text=customCheck.get()).pack()


#Part I: Default checkbox
checkVar = IntVar()
#the logic behind this var is that it will contain the value of the checkbox. the value will be stored here and used in the fucntion


checkBut = Checkbutton(root, text= "Only the courageous can check this box!", variable=checkVar)
#create a variable type checkbutton and declaring it
checkBut.pack()


myButton1 = Button(root, text="Show selected", command=checkStatus).pack() #quick buttons to show the change in the checkboxe value


#Part II personalized checkbox

customCheck = StringVar() #the first difference, instead of creating it as an int, we will create it as a string and customize the values

butCheck = Checkbutton(root, text="Here is for a customized checkbox ! ", variable=customCheck, onvalue="Hello World!", offvalue="I love codding") #second difference, adding onvalue and offvalue
butCheck.deselect() #third difference, adding a deselect function
 #there is a little glitch in tkinter where the box is automatically checked when it's personalized, make sure to let be unchecked by default to avoid the little glitch, you can try your program without it and see what i talk about
butCheck.pack()
#Onvalue means the content of the a checked, checkbox
#offvalue means the content of an unchecked checkbox
#you can personalize and custom those values as you see fit, it can be a string that you can directly copy and use as an input for a function or a print for example, a control varibale loop...etc etc the only limit is whatyou want to do with it

myButton2= Button(root, text="Unique and personalized is here !", command= customStatus).pack()


root.mainloop() #main loop where to run the program
