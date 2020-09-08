#made by Hamza Slaoui Habib
#basic program to create drop down boxes in python using tkinter
#dropdown menus use almost the same logic as checkboxes with a few differences. However, they are complementary to each other in order to present to the user a fluid interface
#Program will show how to implement dropdown boxes and how to use them accordingly
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


#function to show which value of the menu is selected. This logic will allow us to use the content of the dropbox as we see fit
def optionSelected():
    myLabel1= Label(root,text=selected.get()).pack()

#list of of items to select from
#using days of a week as an example
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]

selected = StringVar()#variable where to store the elements of our dropbox
selected.set(options[0]) #to set an option as the default one. Here we are using the first value of the list as default
#the other way to use set is to name directly the element you want to use ex: selected.set("Monday")


dropBox = OptionMenu(root, selected, *options)
#NB: don't forget the * in front of options (you can try to not use * to see the difference)
#if you don't want to use a list you can direcly name the elements you want to select from using the form below
#OptionMenu(root, Selected, "Monday", "Tuesday", ...)
dropBox.pack()

myButton1 = Button(root, text="Click here to show selected item", command=optionSelected).pack()



root.mainloop()
