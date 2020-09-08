#program done by Hamza Slaoui Habib
#Basic program to show how to change an icon in a program and how to upload a picture using tkinter
#beginners guide // functions not optimized
#this guide and the following others in the same file are inspired by the course offered by freecodechamp.org




from tkinter import *
from PIL import ImageTk,Image
#make sure to install Pillow to be allowed to import it, to install pillow in windows use the command pip install pillow
#nb: make sure that you installed python correctly to be able to use this command, (path should be included in the installation)
#we use ImageTk and Image to not be restricted by the type of image we can upload (jpg,png...) as the build-in image in python is very limited


#root where tkinter runs
root = Tk()
root.title("Basic tutorial to run images on python")
root.iconbitmap('c:/users/slaou/desktop/training/basic_gui_tutorials_python/myicons/pp.ico')
#define the path from where to get the icon, if the icon is not in the same folder as the program, you need to define the whole path
#NB: the icon should be an ico picture, which means should be a .ico
root.geometry("400x400") #deciding how big we want our initial window 

my_img=ImageTk.PhotoImage(Image.open("c:/users/slaou/desktop/training/basic_gui_tutorials_python/myicons/wydad.png"))
my_label=Label(image=my_img)
my_label.pack()





button_quit = Button(root,text="Exit Program",command=root.quit)
button_quit.pack()



root.mainloop()
