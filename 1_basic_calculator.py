#program done by Hamza Slaoui Habib
#Basic calculator program to demonstrate simple usage of tkinter
#We will be using a simple calculator to cover the very basics 
#program shows a basic take on widgets and buttons, how to place them using grid and how to connect them to simple functions
#beginners guide // functions not optimized
#this guide and the following others in the same file are inspired by the course offered by freecodechamp.org



from tkinter import *

#root where tkinter runs
root = Tk()
root.title("Basic Calculator")

#Creating entry box where you tap your text
entryWidget=Entry(root,width=35,bd=10, borderwidth=5)
entryWidget.grid(row=0, column=0, columnspan=4, padx=30, pady=40) #placing the entry box in the window


#functions to add the numbers from button input
def button_click(number):
    current=entryWidget.get() #to not loose the previous number, we store it, then add it to the next number
    entryWidget.delete(0,END) #and then delete what's in the box else it will always add. If we don't instead of having 15 we will have 151..Etc
    entryWidget.insert(0, str(current) + str(number))

#clear the screen function
def button_clear():
    entryWidget.delete(0,END) #Clear the input box

#addition function
def button_sum():
    firstNumber= entryWidget.get()
    global f_num #we create a global variable where we store the first result
    global math #for the if statement in the equal button
    math="addition"
    f_num= int(firstNumber)
    entryWidget.delete(0,END)

def button_equal():
    secondNumber=entryWidget.get()
    entryWidget.delete(0,END)
    if math=="addition":
        entryWidget.insert(0,(f_num+int(secondNumber)))
    if math=="substract":
        entryWidget.insert(0,(f_num-int(secondNumber)))
    if math=="multiply":
        entryWidget.insert(0,(f_num*int(secondNumber)))
    if math=="divide":
        entryWidget.insert(0,(f_num/int(secondNumber)))

#divide function, same logic as the addition
def button_divide():
    firstNumber= entryWidget.get()
    global f_num
    global math
    math="divide"
    f_num= int(firstNumber)
    entryWidget.delete(0,END)

#same as before, for substraction
def button_subtract():
    firstNumber= entryWidget.get()
    global f_num
    global math
    math="substract"
    f_num= int(firstNumber)
    entryWidget.delete(0,END)

#multiply function
def button_multiply():
    firstNumber= entryWidget.get()
    global f_num
    global math
    math="multiply"
    f_num= int(firstNumber)
    entryWidget.delete(0,END)

#define the number buttons
button_1=Button(root,text="1", padx=40, pady=20,command=lambda: button_click(1))
button_2=Button(root,text="2", padx=40, pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3", padx=40, pady=20,command=lambda: button_click(3))
button_4=Button(root,text="4", padx=40, pady=20,command=lambda: button_click(4))
button_5=Button(root,text="5", padx=40, pady=20,command=lambda: button_click(5))
button_6=Button(root,text="6", padx=40, pady=20,command=lambda: button_click(6))
button_7=Button(root,text="7", padx=40, pady=20,command=lambda: button_click(7))
button_8=Button(root,text="8", padx=40, pady=20,command=lambda: button_click(8))
button_9=Button(root,text="9", padx=40, pady=20,command=lambda: button_click(9))
button_0=Button(root,text="0", padx=40, pady=20,command=lambda: button_click(0))

#defining the functions buttons

button_sum=Button(root,text="+", padx=39, pady=20,command=button_sum)
button_equal=Button(root,text="=", padx=100, pady=20,command=button_equal)
button_clear=Button(root,text="clear", padx=85, pady=20,command=button_clear)
button_subtract=Button(root,text="-", padx=40.4, pady=20,command=button_subtract)
button_multiply=Button(root,text="*", padx=40, pady=20,command=button_multiply)
button_divide=Button(root,text="/", padx=41, pady=20,command=button_divide)


#put the buttons on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_clear.grid(row=5,column=1,columnspan=2)
button_sum.grid(row=6,column=0)
button_equal.grid(row=6,column=1,columnspan=2)
button_subtract.grid(row=5,column=0)
button_multiply.grid(row=4,column=1)
button_divide.grid(row=4,column=2)




#main loop for the program
root.mainloop()
