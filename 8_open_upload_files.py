#made by Hamza Slaoui Habib
#basic program to open files and load them through file dialog in python using tkinter
#program to select files from the computer and load them
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


#here for example we want first all png files, then all file types
root.filename = filedialog.askopenfilename(initialdir="'c:/", title="Select a file",filetypes=(("png files","*.png"),("all files","*.*")))

#after clicking on open you will load whatever file you selected
#you can then either create an ImageTk for example to load the picture, or get the name etc...
#You can use everything we did before to make it more refined, as in creating buttons, loading images, frames ...etc etc etc

root.mainloop() #main loop
