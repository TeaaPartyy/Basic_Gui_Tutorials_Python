#made by Hamza Slaoui Habib
#basic program to create radio buttons in python using tkinter
#radio buttons are often used to offer choices during interations
#beginners guide // functions not optimized
#this guide and the following others in the same file are inspired by the course offered by freecodechamp.org

from tkinter import *
from PIL import ImageTk,Image

#creating the root
root = Tk()
root.title("basic tutorial to add frames on python") #title
root.iconbitmap('c:/users/slaou/desktop/training/basic_gui_tutorials_python/myicons/pp.ico')
#define the path from where to get the icon, if the icon is not in the same folder as the program, you need to define the whole path
#NB: the icon should be an ico picture, which means should be a .ico
root.geometry("400x400") #deciding how big we want our initial window 

#example is set with radiobuttons to determine which academic standing of students we have
#creating the list with name of the standing of student and its value ("","")
MODES = [
    ("Freshman", "Freshman"),
    ("Sophommore", "Sophommore"),
    ("Junior", "Junior"),
    ("Senior", "Senior"),
]

stud = StringVar()
stud.set("Freshman")
#for loop to create automatically the buttons according to how many standings we have.
for text, mode in MODES:
    Radiobutton(root, text=text, variable =stud, value=mode).pack(anchor=W)

def click(value): #quick function that gets the number of the option we click on
    myLabel = Label(root, text=stud.get())
    myLabel.pack()

#radio buttons creation
#Radiobutton(root, text="Option 1",variable=r,value=1).pack()
#Radiobutton(root, text="Option 2",variable=r,value=2).pack()

#button to get the print of the standing of the option we chose
myButton = Button(root, text="try to click here !",command=lambda:click(stud.get()))
myButton.pack()



mainloop() #mainloop for the program
