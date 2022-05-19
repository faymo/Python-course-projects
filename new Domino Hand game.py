#Author: Fayez Mohammed
#Date: November 12, 2021
#Purpose: Creating a domino class which will allow the creation, manipulation and output of a domino.
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Purpose: to create a domino
#DATA ELEMENTS:
#   value - 0, 66
#   size - 30, 100
#   diameter - size // 5
#   gap - diameter // 2
#   orientation - Horizontal or Vertical
#   faceup status - True or False
#METHOD:
#   __init__
#   getValue
#   setValue
#   flip
#   setOrientation
#   setFace
#   randomize
#   draw
#   __str__

#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import random
from tkinter import *
from tkinter import messagebox

class Domino: 
#   Purpose: to construct the object in the class
#   Parameters : n/a
#   Return/output: n/a
  def __init__(self, value = random.randint(0,66), size = 30, diameter = 40, gap = 20, orientation = "H", faceup = True):
    self.value = value
    self.size = size
    self.diameter = self.size // 5
    self.gap = self.diameter // 2
    self.orientation = orientation
    self.faceup = faceup
    return
#   Purpose: to get a value from the user
#   Parameters : n/a
#   Return/output: value
  def getValue(self):
    try:
      value = int(input("Please enter an integer for size (0-66): "))
      while value > 66 or value < 0:
        print("Please enter an integer from 0-66.")
        value = int(input("Please enter an integer for size (0-66): "))
    except:
      print("An Error has occured. PLEASE enter valid input.")
      value = int(input("Please enter an INTEGER for size (0-66): "))
      while value > 66 or value < 0:
        print("Please enter an integer from 0-66.")
        value = int(input("Please enter an integer for size (0-66): "))
    return value

#   Purpose: to set the value
#   Parameters : n/a
#   Return/output: n/a
  def setValue(self):
    try:
      self.size = self.getValue()    
    except:
      self.size = 0
    return

  def tens(self):
    tens = self.value // 10
    return tens

  def ones(self):
    ones = self.value % 10
    return ones
#   Purpose: to flip the value
#   Parameters : n/a
#   Return/output: the flipped value
  def flip(self):
    value = str(self.value)
    value = value[::-1]
    return int(value)

#   Purpose: to set the orientation
#   Parameters : n/a
#   Return/output: n/a
  def setOrientation(self):
    self.orientation = input("Please enter which way you would like the domino to face('H' or 'V'):" )
    while self.orientation != "H" or self.orientation != "V":
      self.orientation = input("Please enter which way you would like the domino to face('H' or 'V'):" )
    return

#   Purpose: to set the size
#   Parameters : n/a
#   Return/output: n/a
  def setSize(self):
    try:
      self.size = int(input("Please enter your size (30-100): "))
      while self.size > 100 or self.size < 30:
        self.size = int(input("Please enter your size (30-100): "))
    except:
      print("An error has occured. please enter valid input")
      self.size = int(input("Please enter your size (30-100): "))
      while self.size > 100 or self.size < 30:
        self.size = int(input("Please enter your size (30-100): "))
    return

#   Purpose: to set wheter it is face up or face down
#   Parameters : n/a
#   Return/output: n/a
  def setFace(self):
    self.faceup = input("Please enter which way you would like the domino to face('up' or 'down'):" )
    while self.faceup != "up" or self.faceup != "down":
      self.faceup = input("Please enter which way you would like the domino to face('up' or 'down'):" )
    return

#   Purpose: to give a randomized number for value
#   Parameters : n/a
#   Return/output: n/a
  def randomize(self):
    self.value = random.randint(0,66)
    return

#   Purpose: to draw the domino in total
#   Parameters : c, x, y, flip 
#   Return/output: n/a 
  def draw(self, c, x = 0, y = 0, flip = False):
    #flipped or not
    if flip == True:
      value = self.flip()
    else:
      value = self.value
    #First half of domino
    self.drawHalf(c, x, y, value//10)
    #Second half of domino
    if self.orientation == "H":
      self.drawHalf(c, x + self.size, y, value%10)
    else:
      self.drawHalf(c, x, y + self.size, value%10)
    return

#   Purpose: to draw the second half of the domino
#   Parameters : c, x, y, value
#   Return/output: n/a
  def drawHalf(self, c, x, y, value):
    if self.faceup == True:
      c.create_rectangle(x, y, x + self.size, y + self.size, width = 3, outline="black", fill="white")
      if value == 1:
        c.create_oval(x + 4*self.gap, y + 4*self.gap, x + 4*self.gap + self.diameter, y + 4*self.gap + self.diameter, fill ="black")
      elif value == 2:
        c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
        c.create_oval(x + 7*self.gap, y + 7*self.gap, x + 7*self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
      elif value == 3:
        c.create_oval(x + 4*self.gap, y + 4*self.gap, x + 4*self.gap + self.diameter, y + 4*self.gap + self.diameter, fill ="black")
        c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
        c.create_oval(x + 7*self.gap, y + 7*self.gap, x + 7*self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
      elif value == 4:
        c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
        c.create_oval(x + 7*self.gap, y + self.gap, x + 7*self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
        c.create_oval(x + self.gap, y + 7*self.gap, x + self.gap + self.diameter, y + 7*self.gap + self.diameter, fill = "black")
        c.create_oval(x + 7*self.gap, y + 7*self.gap, x + 7*self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
      elif value == 5:
        c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
        c.create_oval(x + 7*self.gap, y + self.gap, x + 7*self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
        c.create_oval(x + 4*self.gap, y + 4*self.gap, x + 4*self.gap + self.diameter, y + 4*self.gap + self.diameter, fill ="black")
        c.create_oval(x + self.gap, y + 7*self.gap, x + self.gap + self.diameter, y + 7*self.gap + self.diameter, fill = "black")
        c.create_oval(x + 7*self.gap, y + 7*self.gap, x + 7*self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
      elif value == 6:
        c.create_oval(x + self.gap, y + self.gap, x + self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
        c.create_oval(x + 7*self.gap, y + self.gap, x + 7*self.gap + self.diameter, y + self.gap + self.diameter, fill ="black")
        c.create_oval(x + self.gap, y + 4*self.gap, x + self.gap + self.diameter, y + 4*self.gap + self.diameter, fill ="black")
        c.create_oval(x + 7*self.gap, y + 4*self.gap, x + 7*self.gap + self.diameter, y + 4*self.gap + self.diameter, fill ="black")
        c.create_oval(x + self.gap, y + 7*self.gap, x + self.gap + self.diameter, y + 7*self.gap + self.diameter, fill = "black")
        c.create_oval(x + 7*self.gap, y + 7*self.gap, x + 7*self.gap + self.diameter, y + 7*self.gap + self.diameter, fill ="black")
    elif self.faceup == False:
       c.create_rectangle(x, y, x + self.size, y + self.size, width = 3, outline="black", fill="gray")
    return

#   Purpose: to get the weight of the domino
#   Parameters : n/a
#   Return/output: n/a
  def getWeight(self):
    firstDigit = int(self.value//10)
    secondDigit = int(self.value%10)
    if firstDigit > secondDigit:
        self.weight = int(str(secondDigit) + str(firstDigit))
    else:
        self.weight = self.value

#   Purpose: to get string
#   Parameters : n/a
#   Return/output: string version
  def __str__(self):
    strDomino = str(self.value)
    return strDomino

#Purpose: A 3 domino game
#DATA ELEMENTS:
#   value - 0, 66
#   size - 30, 100
#   diameter - size // 5
#   gap - diameter // 2
#   orientation - Horizontal or Vertical
#   faceup status - True or False
#METHOD:
#   __init__
#   getValue
#   setValue
#   flip
#   setOrientation
#   setFace
#   randomize
#   draw
#   __str__

#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

class Hand:
    #   Purpose: to construct the object in the class
    #   Parameters : n/a
    #   Return/output: n/a
    def __init__(self, firstDomino = Domino(), secondDomino = Domino(), thirdDomino = Domino(), size = 60):
        if size >= 30 or size <=100:
            self.size = size
        else:
            self.size = 60
        self.firstDomino = Domino(size = size)
        self.secondDomino = Domino(size = size)
        self.thirdDomino = Domino(size = size)
    #   Purpose: to get string
    #   Parameters : n/a
    #   Return/output: string version
    def __str__(self):
        strhand = str(self.firstDomino) + " - " + str(self.secondDomino) + " - " + str(self.thirdDomino)
        return strhand
    
    #   Purpose: sets the size of the domino
    #   Parameters : size
    #   Return/output:
    def setSize(self, size = 60):
        if size >= 30 or size <=100:
            self.size = size
        else:
            size = 60
        self.firstDomino = Domino(size = size)
        self.secondDomino = Domino(size = size)
        self.thirdDomino = Domino(size = size)
        return
    

    #   Purpose: sorting domino lowest to highest
    #   Parameters : n/a
    #   Return/output: n/a
    def sort(self):
        self.firstDomino.getWeight()
        self.secondDomino.getWeight()
        self.thirdDomino.getWeight()
        a = self.firstDomino.value
        b = self.secondDomino.value
        c = self.thirdDomino.value
        if a > b:
            a,b = b,a
        if a > c:
            a,c = c,a
        if b > c:
            b,c = c,b
        self.firstDomino.value = a
        self.secondDomino.value = b
        self.thirdDomino.value = c
    
    #   Purpose: to roll a random number for each of the domino in the hand
    #   Parameters : n/a
    #   Return/output: string version
    def roll(self):
        self.firstDomino.randomize()
        self.secondDomino.randomize()
        self.thirdDomino.randomize()
        
    #   Purpose: to draw the domino on the canvas
    #   Parameters : n/a
    #   Return/output: n/a
    def draw(self, c, x, y):
        self.firstDomino.draw(c,x,y)
        self.secondDomino.draw(c,x*4+self.size, y)
        self.thirdDomino.draw(c, x*8+self.size*1.5,y)
        
    #   Purpose: to get the first and second digit of the domino
    #   Parameters : n/a
    #   Return/output: firstdigit or seconddigit
    def getDigit(self, domino, digit=1):
        firstDigit = int(domino.value//10)
        secondDigit = int(domino.value%10)
        if digit == 1:
            return firstDigit
        else:
            return secondDigit
        
    #   Purpose: to find out wheter the run is 3
    #   Parameters : n/a
    #   Return/output: value
    def run(self):
        value = False
        dominostr = ""
        x = 0
        y = False
        z = 0
        dominostr = str(self.firstDomino.value) + str(self.secondDomino.value) + str(self.thirdDomino.value)
        dominolist = []
        dominolist.append(str(self.firstDomino.value))
        dominolist.append(str(self.secondDomino.value))
        dominolist.append(str(self.thirdDomino.value))
        for c in dominostr:
            for e in dominolist:
                if c in e:
                    x += 1
            if x == 3:
                y = True
            elif x == 2:
                z +=1
            x = 0
        if z >= 3:
            value = True
        elif y == True and z == 2:
            value = True
        return value

    #   Purpose: to find out the run of the hand
    #   Parameters : n/a
    #   Return/output: run 0, 2, or 3
    def getRun(self):
        v1d1 = self.getDigit(self.firstDomino, 1)
        v1d2 = self.getDigit(self.firstDomino, 2)
        v2d1 = self.getDigit(self.secondDomino, 1)
        v2d2 = self.getDigit(self.secondDomino, 2)
        v3d1 = self.getDigit(self.thirdDomino, 1)
        v3d2 = self.getDigit(self.thirdDomino, 2)
        if v1d1 != v2d1 and v1d1 != v2d2 and v1d1 != v3d1 and v1d1 != v3d2 and v1d2 != v2d1 and v1d2 != v2d2 and v1d2 != v3d1 and v1d2 != v3d2 and v2d1 != v3d1 and v2d2 != v3d1 and v2d1 != v3d2 and v2d2 != v3d2:
            return 0
        elif (self.firstDomino.value == self.secondDomino.value == self.thirdDomino.value) or self.run() == True:
            return 3
        else:
            return 2

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-SUB-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= 
def keyPressed(event):
    if event.char == "h" or event.char == "h":
        handOfDomino = Hand()
        handOfDomino.setSize(random.randint(30,100))
        handOfDomino.roll()
        canvas.delete('all')
        handOfDomino.draw(canvas, 50, 10)
        str1.set(handOfDomino)
        handOfDomino.sort()
        handOfDomino.draw(canvas, 50, 200)
        str2.set(handOfDomino)
        dominoRun.set('Run is: ' + str(handOfDomino.getRun()))
    elif event.char == 'g' or event.char == 'G':
        runZero = 0
        runTwo = 0
        runThree = 0
        for i in range(1,10001):
            handOfDominos = Hand()
            handOfDominos.roll()
            run = handOfDominos.getRun()
            if run == 0:
                runZero += 1
            elif run == 2:
                runTwo += 1
            elif run == 3:
                runThree += 1
        zero.set(str(runZero) + ' - ' + str(round(runZero/10000*100, 2)) +
                 '%')
        two.set(str(runTwo) + ' - ' + str(round(runTwo/10000*100, 2)) + '%')
        three.set(str(runThree) + ' - ' + str(round(runThree/10000*100, 2)) + '%')
    else:
        messagebox.showerror("Error", 'Invalid Input')

root = Tk()
root.title('Dominos')
root.config(bg='green')
canvas = Canvas(root, width = 800, height = 350)
canvas.bind('<Key>', keyPressed)
canvas.config(background = 'green')
dominoRun = StringVar()
zero = StringVar()
two = StringVar()
three = StringVar()
str1 = StringVar()
str2 = StringVar()

zerolabel = Label(root, text = 'Amount of run = 0', bg = 'green', font = ("Arial", "12", "bold"))
twolabel = Label(root, text = 'Amount of run = 2', bg = 'green', font = ("Arial", "12", "bold"))
threelabel = Label(root, text = 'Amount of run = 3', bg = 'green', font = ("Arial", "12", "bold"))
runlbl = Label(root, textvariable=dominoRun, bg = 'green', font = ("Arial", "12", "bold"))
str1lbl = Label(root, textvariable=str1, bg = 'green', font = ("Arial", "12", "bold"))
str2lbl = Label(root, textvariable=str2, bg = 'green', font = ("Arial", "12", "bold"))
zerolbl = Label(root, textvariable=zero, bg = 'green', font = ("Arial", "12", "bold"))
twolbl = Label(root, textvariable=two, bg = 'green', font = ("Arial", "12", "bold"))
threelbl = Label(root, textvariable=three, bg = 'green', font = ("Arial", "12", "bold"))
canvas.grid(column=1, row = 0, columnspan=3, rowspan=3)
runlbl.grid(column=2, row=1)
zerolabel.grid(column=1, row=3)
twolabel.grid(column=2, row=3)
threelabel.grid(column=3, row=3)
zerolbl.grid(column=1, row=4)
twolbl.grid(column=2, row=4)
threelbl.grid(column=3, row=4)
str1lbl.place(x = 360, y = 130)
str2lbl.place(x = 360, y = 310)
canvas.focus_set()
mainloop()

