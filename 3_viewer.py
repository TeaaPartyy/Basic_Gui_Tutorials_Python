#program done by Hamza Slaoui Habib
#Basic program to create a viewer for photos, extending the tutorial about how to include pictures in python
#tutorial for beginners (functions not 100% optimized)
#this guide and the following others in the same file are inspired by the course offered by freecodechamp.org





from tkinter import *
from PIL import ImageTk, Image
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


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget() #get rid of previous picture from the screen
    #move to the next image in the list
    my_label = Label(image=image_list[image_number-1]) #it's a -1 because the index of the next item in the list is "1" not "3"
    button_forward= Button(root,text=">>", command=lambda: forward(image_number+1))
    button_back= Button(root,text="<<",command=lambda: back(image_number-1))

    #placing the buttons again on the frame
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
#if we reach the maximum of the list we comeback to the previous one
    if image_number==4:
        image_number=3

#update the status bar
    status= Label(root,text="Image "+ str(image_number) +" of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

#exact same function as the previous one, just we start with the back button this time
def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget() #get rid of previous picture from the screen
    #move to the next image in the list
    my_label = Label(image=image_list[image_number-1]) #it's a -1 because the index of the next item in the list is "1" not "3"
    button_forward= Button(root,text=">>", command=lambda: forward(image_number+1))
    button_back= Button(root,text="<<",command=lambda: back(image_number-1))

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    my_label.grid_forget() #get rid of previous picture from the screen

#move to the next image in the list
    my_label = Label(image=image_list[image_number-1]) #it's a -1 because the index of the next item in the list is "1" not "3"
    button_forward= Button(root,text=">>", command=lambda: forward(image_number+1))
    button_back= Button(root,text="<<",command=lambda: back(image_number-1))

#placing the buttons on the frame
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    if image_number==0:
        button_back= Button(root,text="<<",state=DISABLED)

    status= Label(root,text="Image "+ str(image_number) +" of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)

#upload images
my_img1=ImageTk.PhotoImage(Image.open("c:/users/slaou/desktop/training/basic_gui_tutorials_python/myicons/wydad.png"))
my_img2=ImageTk.PhotoImage(Image.open("c:/users/slaou/desktop/training/basic_gui_tutorials_python/myicons/wid2.png"))
my_img3=ImageTk.PhotoImage(Image.open("c:/users/slaou/desktop/training/basic_gui_tutorials_python/myicons/wyd3.png"))
my_img4=ImageTk.PhotoImage(Image.open("c:/users/slaou/desktop/training/basic_gui_tutorials_python/myicons/wyd4.png"))


#create list of images
image_list=[my_img1, my_img2, my_img3, my_img4]

#creating a status bar

status= Label(root,text="Image 1 of "+str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)


#placing the image in the frame
my_label=Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)



#create scrolling buttons
button_back= Button(root,text="<<", command=lambda: back())
button_exit=  Button(root, text="Exit Program",command=exit)
button_forward= Button(root,text=">>", command= lambda: forward(2))

#putting the buttons in the frame
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2,pady=10)

#putting the status bar in the frame

status.grid(row=2,column=0,columnspan=3,sticky=W+E)



root.mainloop()
