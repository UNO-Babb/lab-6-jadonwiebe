#DiceRoll.py
#Name:Jadon Wiebe
#Date:10/05
#Assignment:Dice Rolls
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1, 6)
    rolls[(dice1 + dice2) - 1] = rolls[(dice1 + dice2) - 1] + 1
    
  #find the sum total of the two dice

  #print statictics for dice rolls
  dice = 1
  for count in rolls:
    percent = (count/10000) * 100
    print(dice, ":" , count, " - ", round(percent, 1), "percent")
    dice = dice + 1

if __name__ == '__main__':
  main()
