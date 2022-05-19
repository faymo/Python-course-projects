#Author: Fayez Mohammed
#Date: October 29th, 2021
#Purpose: To make patterns in different shapes and sizes that are filled or hollow using GUI
#-----------------------------------------------------------------------------

#GUI
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Star Patterns")
window.geometry("500x550")
intsize = IntVar()
objshape = StringVar()
bolhollow = BooleanVar()

#Square Pattern
def displaysquare_filled(size = 1):
  labelpattern.config(text = "Square Star Pattern: ") 
  for i in range(size):
    for i in range(size):
        textpattern.insert(END, "* ")
    textpattern.insert(END, " " + "\n")

#Hollow Square Pattern
def displaysquare_hollow(size = 1):
  labelpattern.config(text = "Hollow Square Star Pattern: ")  
  for i in range(size):
    for j in range(size):
        if i == 0 or i == size -1  or j == 0 or j == size - 1:
          textpattern.insert(END, "* ")
        else:
          textpattern.insert(END, "  ")
    textpattern.insert(END, " " + "\n")

#Triangle Pattern
def displaytriangle_filled(size = 1):
  labelpattern.config(text = "Triangle Star Pattern: ") 
  for i in range(0, size):  
    for j in range(0, i + 1):   
      textpattern.insert(END, "* ")       
    textpattern.insert(END, " " + "\n")  

#Hollow Triangle Pattern
def displaytriangle_hollow(size = 1):
  labelpattern.config(text = "Hollow Triangle Star Pattern: ") 
  for i in range(size):
    for j in range(i+1):
        if j == 0 or j == i or i == size - 1:
            textpattern.insert(END, "* ")
        else:
            textpattern.insert(END, "  ")
    textpattern.insert(END, " " + "\n")

#Diamond Pattern
def displaydiamond_filled(size = 1):
  if size % 2 == 1:
    labelpattern.config(text = "Diamond Star Pattern: ")
    #upper half
    for a1 in range(1, (size+1)//2 + 1): 
      for a2 in range((size+1)//2 - a1):
          textpattern.insert(END, " ")
      for a3 in range((a1*2)-1):
          textpattern.insert(END, "*")
      textpattern.insert(END, " " + "\n")
    #lower half
    for a1 in range((size+1)//2 + 1, size + 1): 
      for a2 in range(a1 - (size+1)//2):
          textpattern.insert(END, " ")
      for a3 in range((size+1 - a1)*2 - 1):
          textpattern.insert(END, "*")
      textpattern.insert(END, " " + "\n")
  else:
    var = messagebox.showerror("Invalid Input", "Please enter an odd size for a diamond shape")

#Hollow Diamond Pattern
def displaydiamond_hollow(size = 1):
  labelpattern.config(text = "Hollow Diamond Star Pattern: ")
  if size % 2 == 1:
    # Upper part of hollow diamond
    for i in range(1, size + 1):
      for j in range(1, size - i + 1):
          textpattern.insert(END, " ")
      for j in range(1, 2 * i):
          if j == 1 or j == 2 * i - 1:
              textpattern.insert(END, "*")
          else:
              textpattern.insert(END, " ")
      textpattern.insert(END, " " + "\n")

    # Lower part of hollow diamond
    for i in range(size - 1 , 0, -1):
      for j in range(1, size - i + 1):
          textpattern.insert(END, " ")
      for j in range(1, 2 * i):
          if j == 1 or j == 2 * i - 1:
              textpattern.insert(END, "*")
          else:
              textpattern.insert(END, " ")
      textpattern.insert(END, " " + "\n")
  else:
    var = messagebox.showerror("Invalid Input", "Please enter an odd size for a diamond shape")

#Draw button function
def create():
  clear()
  shape = objshape.get()
  hollow = bolhollow.get()
  size = intsize.get()
  if shape == "Square" and hollow == False:
    displaysquare_filled(size)
  elif shape == "Square" and hollow == True:
    displaysquare_hollow(size)
  elif shape == "Triangle" and hollow == False:
    displaytriangle_filled(size)
  elif shape == "Triangle" and hollow == True:
    displaytriangle_hollow(size)
  elif shape == "Diamond" and hollow == False:
    displaydiamond_filled(size)
  elif shape == "Diamond" and hollow == True:
    displaydiamond_hollow(size)

#Clear button function
def clear():
  textpattern.delete(1.0, END)

#GUI------------------------------------------------------------------------------------------------------------
labelshape = Label(window, text = "Select your shape:")
frameshape = Frame(window, relief = GROOVE, bd = 3
radiosquare = Radiobutton(frameshape, text = "Square", variable = objshape, value = "Square")
radiotriangle = Radiobutton(frameshape, text = "Triangle", variable = objshape, value = "Triangle")
radiodiamond = Radiobutton(frameshape, text = "Diamond", variable = objshape, value = "Diamond")
labelhollow = Label(window, text = "Do you want your shape \n to be filled or hollow:")
framehollow = Frame(window, relief = GROOVE, bd = 3)
radiofilled = Radiobutton(framehollow, text = "Filled", variable = bolhollow, value = False)
radiohollow = Radiobutton(framehollow, text = "Hollow", variable = bolhollow, value = True)
labelsize = Label(window, text = "Select the size for your shape:")
scalesize = Scale(window, to = 20, variable = intsize, relief = GROOVE)
buttonclear = Button(window, text = "Clear Drawing", width = 17, command = lambda: clear())
buttondraw = Button(window, text = "Draw Your Shape", width = 17, command = lambda: create())
buttonexit = Button(window, text = "Exit the Program", width = 17, command = lambda: quit())
labelpattern = Label(window, text = "Pattern:")
textpattern = Text(window, height = 20, width = 42, relief = FLAT)

labelshape.grid(columnspan = 1, rowspan = 1, padx = 25)
frameshape.grid(columnspan = 1, rowspan = 1, row = 2, column = 0, pady = 5)
radiosquare.grid(sticky = W)
radiotriangle.grid(sticky = W)
radiodiamond.grid(sticky = W)
labelhollow.grid(columnspan = 1, rowspan = 1, column = 1, row = 0)
framehollow.grid(columnspan = 1, rowspan = 1, row = 2, column = 1, pady = 5)
radiofilled.grid(sticky = W)
radiohollow.grid(sticky = W)
labelsize.grid(columnspan = 1, rowspan = 1, column = 2, row = 0, padx = 25)
scalesize.grid(columnspan = 1, rowspan =  1, column = 2, row = 2)
buttonclear.grid(column = 0, row = 3, pady = 10)
buttondraw.grid(column = 1, row = 3, pady = 10)
buttonexit.grid(column = 2, row = 3, pady = 10)
labelpattern.grid(column = 1, row = 4)
textpattern.grid(column = 0, row = 5, columnspan = 3, rowspan = 3, sticky = W, padx = 75)
