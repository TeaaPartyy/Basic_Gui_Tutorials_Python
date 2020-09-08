#made by Hamza Slaoui Habib
#basic program to create a frame in python using tkinter
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

my_frame= LabelFrame(root, text="This is a frame", padx=50, pady=50) #creating the frame   // pady and pady for the interior pathing of the frame
my_frame.pack(padx=10, pady=10)    #the padx/pady is for the exterior pathing of the frame
#nb: keep in mind that you can play with the numbers of padx and pady in order to design it the way you want



#skip this function until you read the button (you can skip it entirely, not needed to create a frame)
#function is to add a label for a fun interaction in case someone clicks the button bellow
def touchy():
    my_label = Label(my_frame,text="you naughty!!")
    my_label.pack()

 #fill the frame with a button/Label.. whatever you want to see in your frame
b= Button(my_frame, text="no touchy / pas touche",command=touchy)
b.pack()


mainloop() #main loop of the root
