#Author: Fayez Mohammed
#Date: November 9th, 2021
#Purpose: Making a Calender using Classes
#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

#Purpose: A date
#DATA ELEMENTS:
#   day - 1, maxDays
#   month - 1, 12
#   year - 1600, 2200
#METHOD:
#   __init__
#   returnMonthName
#   returnLeapYear
#   returnMaxDay
#   calcZeller
#   returnDayName
#   calcValid
#   getDate
#   __str__
#   displayCalendar

#=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
import random

class Date: 
#   Purpose: to construct the object in the class
#   Parameters : n/a
#   Return/output: n/a
  def __init__(self, day = 1, month = 1, year = 2019):
    self.day = day
    self.month = month
    self.year = year
    self.calcValid()

#   Purpose: to convert the data element to string
#   Parameters : n/a
#   Return/output: string of month
  def returnMonthName(self):
    m = self.month
    if m == 1:
      month = "January"
    elif m == 2:
      month = "Febuary"
    elif m == 3:
      month = "March"
    elif m == 4:
      month = "April"
    elif m == 5:
      month = "May"
    elif m == 6:
      month = "June"
    elif m == 7:
      month = "July"
    elif m == 8:
      month = "August"
    elif m == 9:
      month = "September"
    elif m == 10:
      month = "October"
    elif m == 11:
      month = "November"
    elif m == 12:
      month = "December"
    return month

#   Purpose: to find out wheter the year is a leap year or not
#   Parameters : n/a
#   Return/output: true or false for leap year
  def returnLeapYear(self, x = 0):
    if x == 0:
      year = self.year
    else:
      year = x
    if(year % 400 == 0) and (year % 100 == 0):
      leap = True
    elif (year % 100 != 0) and (year % 4 == 0):
      leap = True
    else:
      leap = False
    return leap

#   Purpose: to find the maximum days in a month
#   Parameters : n/a
#   Return/output: maximum days in the month
  def returnMaxDay(self, x = 0):
    if x != 0:
      m = x
    else:
      m = self.month
    leap = self.returnLeapYear()
    if m == 4 or m == 6 or m == 9 or m == 11:
      days = 30
    elif m == 2:
      if leap == True:
        days = 29
      else:
        days = 28
    else:
      days = 31
    return days

#   Purpose: to find what day the number is on
#   Parameters : n/a
#   Return/output: 0-6 representing day of week
  def calcZeller(self):
    m = self.month - 2
    y = self.year
    if m <= 0:
      m = m + 12
      y = y - 1
    p = y // 100
    r = y % 100
    return (self.day + (26 * m - 2) // 10 + r + r // 4 + p // 4 + 5 * p) % 7

#   Purpose: changes day element to string counterpart
#   Parameters : n/a
#   Return/output: string conversion
  def returnDayName(self):
    day = self.calcZeller()
    if day == 0:
      name = "Sunday"
    elif day == 1:
      name = "Monday"
    elif day == 2:
      name = "Tuesday"
    elif day == 3:
      name = "Wednesday"
    elif day == 4:
      name = "Thursday"
    elif day == 5:
      name = "Friday"
    elif day == 6:
      name = "Saturday"
    return name

#   Purpose: to make sure the data elements are valid
#   Parameters : n/a
#   Return/output: wheter the data element is valid or not
  def calcValid(self):
    try:
      Validay = False
      Validmonth = False
      Validyear = False
      Valid = False
      
      if str(self.day).isdigit():
        if self.day >= 1 or self.day <= 31:
          Validay = True
      
      if str(self.month).isdigit():
        if self.month >= 1 or self.month <= 12:
          Validmonth = True
      
      if str(self.year).isdigit():
        if self.year >= 1600 or self.year <= 2200:
          Validyear = True

      if Validyear == True and Validmonth == True and Validay == True:
        Valid = True

    except:
      Valid = False
    return Valid

#   Purpose: to find out wheter the data elements of the object are positive or not.
#   Parameters : n/a
#   Return/output: positive integer
  def getPositiveInteger(self):
    try: 
      positive =  True
      day =  self.day
      month = self.month
      year = self.year
      if not (str(day).isdigit()) or day < 0:
        positive = False
      if not (str(month).isdigit()) or month < 0:
        positive = False
      if not (str(year).isdigit()) or year < 0:
        positive = False
    except:
      positive = False
    return positive

#   Purpose: to get the input of date from the user.
#   Parameters : n/a
#   Return/output: outputs valid year, month, and day to use. 
  def getDate(self):
    self.day = int(input("Please enter the day (1-31): " ))
    self.month = int(input("Please enter the month (1-12): "))
    self.year = int(input("Please enter the year (1600-2200): "))
    valid = self.calcValid()
    positive = self.getPositiveInteger()
    while valid == False or positive == False:
      print("Your number is not valid or positive. Please enter new valid inputs.")
      self.day = int(input("Please enter the day: " ))
      self.month = int(input("Please enter the month: "))
      self.year = int(input("Please enter the year: "))
      valid = self.calcValid()
      positive = self.getPositiveInteger()
    
#   Purpose: to convert and prepare object for Print() usage
#   Parameters : n/a
#   Return/output: string conversion
  def __str__(self):
    dayname = self.returnDayName()
    monthname = self.returnMonthName()
    strDate = str(dayname) + ", " + str(monthname) + " " + str(self.day) + ", " + str(self.year)
    return strDate

#   Purpose: to convert the data element to string
#   Parameters : n/a
#   Return/output: string of month
  def random(self):
    self.day = random.randint(1, 30)
    self.month = random.randint(1, 12)
    self.year = random.randint(1600, 2200)

#   Purpose: to make a calender using the inputted date and other methods
#   Parameters : n/a
#   Return/output: the calender
  def displayCalender(self):
    self.day = 1
    day = self.calcZeller() - 1
    space = ''
    space = space.rjust(3, ' ')      
    monthname = self.returnMonthName()
    print("        ", monthname, self.year)
    print('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
    if self.month == 9 or self.month == 4 or self.month == 6 or self.month == 11: 
      for i in range(31 + day):
        if i<= day:
          print(space, end =' ')
        else:
          print("{:02d}".format(i-day), end ='  ')
        if (i + 1)% 7 == 0:
          print()
    elif self.month == 2:
      if self.returnLeapYear() == True:
        p = 30
      else:
        p = 29
                
      for i in range(p + day):
        if i<= day:
          print(space, end =' ')
        else:
          print("{:02d}".format(i-day), end ='  ')
        if (i + 1)% 7 == 0:
          print() 
    else:
      for i in range(32 + day):
        if i<= day:
          print(space, end =' ')
        else:
          print("{:02d}".format(i-day), end ='  ')
          if (i + 1)% 7 == 0:
            print()

#   Purpose: to find out days in a year
#   Parameters : x, y
#   Return/output: days in the year
  def dayOfYear(self, x, y):
    month = 1
    dayOfYear = 0
    for month in range(1, x+1):
      dayOfYear += self.returnMaxDay(month)
    dayOfYear += y
    return dayOfYear
  
#   Purpose: to find out if a date is greater than another.
#   Parameters : secondDate
#   Return/output: true or false
  def __gt__(self, secondDate):
      answer = False
      if self.day > secondDate.day:
        answer = True
      if self.month > secondDate.month:
        answer = True
      else:
        answer = False
      if self.year > secondDate.year:
        answer = True
      else:
        answer = False
      return answer

#   Purpose: to find out if a date is less than another.
#   Parameters : secondDate
#   Return/output: true or false
  def __lt__(self, secondDate):
      answer = False
      if self.day < secondDate.day:
        answer = True
      if self.month < secondDate.month:
        answer = True
      else:
        answer = False
      if self.year < secondDate.year:
        answer = True
      else:
        answer = False
      return answer

#   Purpose: to find out if a date is greater than or equal to another.
#   Parameters : secondDate
#   Return/output: true or false
  def __ge__(self, secondDate):
      if self.__gt__(secondDate) == True or self.__eq__(secondDate) == True:
        answer = True
      else:
        answer = False
      return answer

#   Purpose: to find out if a date is less than or equal to another.
#   Parameters : secondDate
#   Return/output: true or false
  def __le__(self, secondDate):
      if self.__lt__(secondDate) == True or self.__eq__(secondDate) == True:
        answer = True
      else:
        answer = False
      return answer

#   Purpose: to find out if a date is equal to another.
#   Parameters : secondDate
#   Return/output: true or false
  def __eq__(self, secondDate):
      answer = True
      if self.year != secondDate.year:
        answer = False
      if self.month != secondDate.month:
        answer = False
      if self.day != secondDate.day:
        answer = False
      return answer

#   Purpose: to find out if a date is not equal to another.
#   Parameters : secondDate
#   Return/output: true or false
  def __ne__(self, secondDate):
      if self.__eq__(secondDate) == True:
        answer = False
      else:
        answer = True
      return answer
    
#   Purpose: to subtract a date from another
#   Parameters : secondDate
#   Return/output: subtracted value
  def __sub__(self, secondDate):
      year_one = int(self.year)
      year_two = int(secondDate.year)
      day_one = self.dayOfYear(self.month, self.day)
      day_two = self.dayOfYear(secondDate.month, secondDate.day)
      if year_one == year_two:
        day_one, day_two = min(day_two, day_one), max(day_one, day_two)
        return day_two - day_one
      if year_one>year_two:
        year_one,year_two = year_two,year_one
        day_one,day_two = day_two,day_one
      if self.returnLeapYear(year_one):
        total = 366 - day_one
      else:
        total = 365 - day_one
      for y in range(year_one+1, year_two):
          if self.returnLeapYear(y):
            total += 366
          else:
            total += 365
      return total + day_two


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-MAIN=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Continue = 'Yes'
while Continue == 'Yes' or Continue == 'yes':

    print("-----------------------------------------")
    date1 = Date()
    date2 = Date()
    date1.getDate()
    date2.getDate()
    print("-----------------------------------------")
    print("Your first date is", date1)
    print("Your second date is", date2)
    print("-----------------------------------------")
    print("first date is greater than second date: ", date1.__gt__(date2))
    print("first date is less than second date: ", date1.__lt__(date2))
    print("first date is greater than or equal to second date: ", date1.__ge__(date2))
    print("first date is less than or equal to second date: ", date1.__le__(date2))
    print("first date is equal to second date: ", date1.__eq__(date2))
    print("first is not equal to second date: ", date1.__ne__(date2))
    print("Your subtracted date is: ", date1.__sub__(date2))
    Continue = input("Again? (Yes/No)    ")
    print("----------------------------------------------")
    while not(Continue == 'Yes' or Continue == 'No' or Continue == 'yes'):
        Continue = input("Again? (Yes/No)    ")

