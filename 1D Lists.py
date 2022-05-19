#Author: Fayez Mohammed
#Date: January 10th, 2022
#Purpose: To manage lists and manipulate them as a object
#---------------------------------------------------------------------

#Purpose: to create group of integers using lists
#DATA ELEMENTS:
#   intList
#   size
#METHOD:
#   __init__
#   __str__
#   initAsNum
#   initAsSeq
#   calcTotal
#   calcMean
#   findLargest
#   calcFreq
#   insertAt
#   removeAt
#   removeAll
#   findFirst
#   isSorted
#---------------------------------------------------------------------
import random

class IntGroup:
#   Purpose: to construct the object in the class
#   Parameters : size
#   Return/output: n/a
    def __init__(self, size = 0):
        if size >= 0 or size <= 20:
            self.size = size
        else:
            size = 0
        self.intList = []
        for e in range(0, size):
            self.intList.append(e)
        
#   Purpose: to print string version of list and size
#   Parameters : n/a
#   Return/output: string
    def __str__(self):
        return str(self.intList) + " size: " + str(self.size)

#   Purpose: to construct the object of the class using input from user
#   Parameters : size, intList
#   Return/output: n/a
    def initAsNum(self, size, intList):
        self.size = size
        self.intList = intList

#   Purpose: to construct the object of the class using size from user and making a sequence list
#   Parameters : size
#   Return/output: n/a
    def initAsSeq(self, size):
        self.size = size
        intList = []
        for i in range(1, size + 1):
            intList.append(i)
        self.intList = intList

#   Purpose: to calculate total of the integers of the list
#   Parameters : n/a
#   Return/output: total
    def calcTotal(self):
        return sum(self.intList)

#   Purpose: to calculate the mean of the integers of the list
#   Parameters : n/a
#   Return/output: Mean
    def calcMean(self):
        sumOfList = sum(self.intList)
        lenOfList = len(self.intList)
        return sumOfList / lenOfList

#   Purpose: to find the largest element in the list
#   Parameters : n/a
#   Return/output: largest element
    def findLargest(self):
        x = 0
        for e in self.intList:
            if e > x:
                x = e
        return x

#   Purpose: to calculate the number of times an element is in a list
#   Parameters : x
#   Return/output: count
    def calcFreq(self, x):
        count = 0
        for e in self.intList:
            if e == x:
                count += 1
        return count

#   Purpose: to insert a value at a specific position in the list
#   Parameters : value, position
#   Return/output: n/a
    def insertAt(self, value, position):
        if position < 0:
            position = 0
        elif position > self.size + 1:
            position = self.size + 1
        self.intList.insert(position - 1, value)
        self.size += 1

#   Purpose: to remove a value at a specific position in the list
#   Parameters : position
#   Return/output: n/a
    def removeAt(self, position):
        del self.intList[position - 1]
        self.size -= 1

#   Purpose: to remove all of a value in the list
#   Parameters : value
#   Return/output: n/a
    def removeAll(self, value):
        intList = []
        count = 0
        for e in self.intList:
            if e != value:
                intList.append(e)
            elif e == value:
                count += 1
        self.intList = intList
        self.size = self.size - count

#   Purpose: to find the first instance of a value in the list
#   Parameters : value
#   Return/output: position
    def findFirst(self, value):
        if value in self.intList:
            position = self.intList.index(value) + 1
        else:
            position = -1
        return position

#   Purpose: to see if the list is sorted or not
#   Parameters : n/a
#   Return/output: true or false
    def isSorted(self):
        isSorted = True
        intList = self.intList
        for i in range(len(intList)):
            for index in range(0+i, len(intList)):
                if intList[i] > intList[index]:
                    isSorted = False
        return isSorted


#------------------------------------MAIN--------------------------------------

Continue = "Yes"

while Continue == "Yes" or Continue == "Y" or Continue == "y" or Continue =="yes":
    listNum = IntGroup()
    listSeq = IntGroup()
    tempList = []
    sizeNum = int(input("What size do you want for normal list?: "))
    sizeSeq = int(input("What size do you want for sequence list?: "))
    randomInput = input("Do you want a randomized list or do you want to input numbers? Y/N?: ")
    if randomInput == "Y" or randomInput == "y":
        for n in range(sizeNum):
            y = random.randint(0, sizeNum)
            tempList.append(y)
    else:
        for n in range(sizeNum):
            x = int(input("Enter your number: "))
            tempList.append(x)
    listNum.initAsNum(sizeNum, tempList)
    listSeq.initAsSeq(sizeSeq)
    print("-----------------------------------------------------------------------------")
    print(listNum)
    print(listSeq)
    print("-----------------------------------------------------------------------------")
    totalNum = listNum.calcTotal()
    totalSeq = listSeq.calcTotal()
    print("Normal total is: ", totalNum)
    print("Sequenece total is: ", totalSeq)
    meanNum = listNum.calcMean()
    meanSeq = listSeq.calcMean()
    print("Normal Mean is: ", totalNum)
    print("Sequenece Mean is: ", totalSeq)
    print("-----------------------------------------------------------------------------")
    largestNum = listNum.findLargest()
    largestSeq = listSeq.findLargest()
    print("The largest element in normal is: ", largestNum)
    print("The largest element in sequence is: ", largestSeq)
    valueNum = int(input("What number do you want to check for frequency with in normal?: "))
    valueSeq = int(input("What number do you want to check for frequency with in sequence?: "))
    freqNum = listNum.calcFreq(valueNum)
    freqSeq = listSeq.calcFreq(valueSeq)
    print(valueNum, "is in normal this many times: ", freqNum)
    print(valueSeq, "is in sequence this many times: ", freqSeq)
    print("-----------------------------------------------------------------------------")
    valueNum = int(input("What element do you want to insert in normal?: "))
    positionNum = int(input("Which position?: "))
    valueSeq = int(input("What number do you want to insert in sequence?: "))
    positionSeq = int(input("Which position?: ")) 
    listNum.insertAt(valueNum, positionNum)
    listSeq.insertAt(valueSeq, positionSeq)
    print("New lists:")
    print(listNum)
    print(listSeq)
    print("-----------------------------------------------------------------------------")
    positionNum = int(input("What position do you want to remove at in normal?: "))
    positionSeq = int(input("What position do you want to remove at in sequence?: "))
    listNum.removeAt(positionNum)
    listSeq.removeAt(positionSeq)
    print("New lists:")
    print(listNum)
    print(listSeq)
    print("-----------------------------------------------------------------------------")
    valueNum = int(input("What element do you want to remove all of in normal?: "))
    valueSeq = int(input("What element do you want to remove all of in sequence?: "))
    listNum.removeAll(valueNum)
    listSeq.removeAll(valueSeq)
    print("New lists:")
    print(listNum)
    print(listSeq)
    print("-----------------------------------------------------------------------------")
    positionNum = int(input("What position do you want to find first of in normal?: "))
    positionSeq = int(input("What position do you want to find first of in sequence?: "))
    firstNum = listNum.findFirst(positionNum)
    firstSeq = listSeq.findFirst(positionSeq)
    print(positionNum, "is first found at: ", firstNum)
    print(positionSeq, "is first found at: ", firstSeq)
    print("-----------------------------------------------------------------------------")
    sortedNum = listNum.isSorted()
    sortedSeq = listSeq.isSorted()
    print("Normal list is sorted?: ", sortedNum)
    print("Sequence list is sorted?: ", sortedSeq)
    print("-----------------------------------------------------------------------------")
    Continue = input("Do you want to try again? Y/N: ")
                 
