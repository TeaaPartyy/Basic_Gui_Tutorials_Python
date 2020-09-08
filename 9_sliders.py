#made by Hamza Slaoui Habib
#basic program to sliders in python using tkinter
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


#the slider itself is a widget. The name of the slider is Scale Widget (in python).
#The default slider is the up & down one.
verticalSlider = Scale(root, from_=0, to=400)
verticalSlider.pack()
#you can design the scale of the slider as you want
#you can also personalize the design in terms of color, background, scale... etc etc as we did with labels before

horizontalSlider = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontalSlider.pack()

#creating a function that will change the size of our window depending on the value of the sliders we want

def slideVertical():
    myLabel= Label(root, text=verticalSlider.get()).pack()
    root.geometry(str(verticalSlider.get()) + "x400")

def slideHorizontal():
    myLabel = Label(root, text=horizontalSlider.get()).pack()
    root.geometry("400x" +str(horizontalSlider.get()))

myButton1= Button(root, text="Click here to change the vertical scale", command=slideVertical).pack()
myButton2= Button(root,text="Click here to change the horizontal scale", command=slideHorizontal).pack()


mainloop() #main loop where the program will be run
