#Author: Fayez Mohammed
#Date: October 16th, 2021
#Purpose: Using 2 prompted positive integers, print permutations, combinations, GCM, LCM, or if they are relatively prime.
#------------------------------------------------------------------------------------------------------------------

#Functions-------------------------------------------------------------------------------------
import random

class TwoCard:
  def __init__(self, card1 = 1, card2 = 1):
    self.card1 = card1
    self.card2 = card2
#To generate a random number to simulate a random card from a deck
        
def getCard():
  return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"])

#To generate a player's hand of 2 cards

def getHand():
  playerHand = TwoCard()
  playerHand.card1 = getCard()
  playerHand.card2 = getCard()
  return playerHand

#To print their hand with suits
def printHand(playerHand):
  suit = random.choice(["♥", "♦", "♣", "♠"])
  suit2 = random.choice(["♥", "♦", "♣", "♠"])
  print("You first card is ", playerHand.card1, suit)
  print("Your second card is ", playerHand.card2, suit2)
  return playerHand

#converting the letters into numbers so I can caluclate spread and payout
def cardconverter(playerHand):
  if playerHand.card1 == "Jack":
    playerHand.card1 = 11
  elif playerHand.card1 == "Queen":
    playerHand.card1 = 12
  elif playerHand.card1 == "King":
    playerHand.card1 = 13
  elif playerHand.card1 == "Ace":
    playerHand.card1 = 14
  elif playerHand.card2 == "Jack":
    playerHand.card2 = 11
  elif playerHand.card2 == "Queen":
    playerHand.card2 = 12
  elif playerHand.card1 == "King":
    playerHand.card2 = 13
  elif playerHand.card2 == "Ace":
    playerHand.card2 = 14
  return playerHand

#To find out the hand type
def handType(playerHand):
  playerHand = cardconverter(playerHand)
  if playerHand.card1 == playerHand.card2:
    print("Your hand type is pair.")
    handtype = "pair"
  elif playerHand.card1 == playerHand.card2 - 1 or playerHand.card1 - 1 == playerHand.card2:
    print("Your hand type is consecutive")
    handtype = "consecutive"
  else:
    print("Your hand type is non-consecutive")
    handtype = "non-consecutive"
  return handtype

#To find the spread of their hand
def spread(playerHand, handtype):
  if handtype == "pair" or handtype == "consecutive":
    cardspread = 0
  else:
    if playerHand.card1 >= playerHand.card2:
      cardspread = playerHand.card1 - playerHand.card2
    else:
      cardspread = playerHand.card2 - playerHand.card1
  return cardspread

#To find the payout
def payout(spread):
  if spread == 1:
    cardpayout = 5
  elif spread == 2:
    cardpayout = 4
  elif spread == 3:
    cardpayout = 2
  elif spread >= 4:
    cardpayout = 1
  return cardpayout

#To find out whether the third card is between the first and second card.
def between(playerHand):
  thirdcard = random.randint(2, 15)
  print("Your third card is ", thirdcard)
  if thirdcard >= playerHand.card1 and thirdcard <= playerHand.card2 or thirdcard >= playerHand.card2 and thirdcard <= playerHand.card1:
    cardbetween = True
    print("Your third card is between card one and card two.")
  else:
    cardbetween = False
    print("Your third card is not between card one and card two.")
  return thirdcard

#Main------------------------------------------------------------------
purse = 100
Decision = "Y"
while Decision == "Y" and purse >= 0:
  bet = int(input("Enter your bet amount: "))
  while bet > purse or bet < 1:
    bet = int(input("Please enter a bet amount less than your purse or more than one: "))
  playerHand = getHand()
  printHand(playerHand)
  handtype = handType(playerHand)
  if handtype == "pair":
    thirdcard = between(playerHand)
    if thirdcard == playerHand.card1 and thirdcard == playerHand.card2:
      purse = purse + bet * 11
      print("You have won 11 times your bet!")
    else:
      print("Your hand was a tie")
  elif handtype == "consecutive":
    print("Your hand was a tie")
  elif handtype == "non-consecutive":
    limit = purse - bet
    newbet = int(input("Please enter another bet between 0 and bet:"))
    while newbet <= 0 or newbet >= limit:
      newbet = int(input("Please enter another bet between 0 and bet:"))
    bet = newbet + bet
    thirdcard = between(playerHand)
    if thirdcard >= playerHand.card1 and thirdcard <= playerHand.card2 or thirdcard >= playerHand.card2 and thirdcard <= playerHand.card1:
      print("You have won the bet!")
      spread = spread(playerHand, handtype)
      payoff = payout(spread)
      purse = purse + bet * payoff
    else:
      print("You have lost your bet")
      purse = purse - bet
  print("Your current balance is", purse)
  Decision = input("Would you like to continue the game? ('Y' for yes, 'N' for no): ")
  while Decision != "Y" and Decision != "N":
    print("Please enter Y or N")
    Decision = input("Would you like to continue the game? ('Y' for yes, 'N' for no): ")

if Decision == "N":
  print("You have stopped playing the game. Have a good day!")

if purse <= 0:
  print("You have ran out of money. Game over.")

