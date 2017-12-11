#  File: Craps.py

#  Description: This program simulates a game of craps. Takes the number of rounds as inputs and outputs the number of time the player wins

#  Student Name: Brian Tsai
	
#  Student UT EID: byt76

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 2/17/17

#  Date Last Modified: 2/17/17
# simulate a single round of craps and
# return 1 if player wins and 0 if he loses

import random
def craps ():
	# The player rolls the dices the first round
	# Return 1 if the player wins and 0 if he loses
  
	# Generates a number between 2 and 12 and stores in come_out_roll
  come_out_roll = random.randint(1,6) + random.randint(1,6) 	
  
  # If the player gets a score of either 7 or 11, then he wins
  if (come_out_roll == 7 or come_out_roll == 11): 
    return 1

  # If the player gets a score of either 2,3 or 12, then he loses 
  elif (come_out_roll == 2 or come_out_roll == 3 or come_out_roll == 12): 
    return 0
  
  # If the player gets any other score, then he plays the second round
  else: 

  	# The player continues to roll until he gets either his first score or a 7 
    while (True): 
      
      # Generates a number between 2 and 12 and stores in point_roll
      point_roll = random.randint(1,6) + random.randint(1,6)	
      
       # If the player rolls their original score first, then the player wins
      if (point_roll == come_out_roll):
        return 1

      # If the player rolls a 7 first, then the player loses  
      elif (point_roll == 7): 
        return 0

      # Keep rolling until the player either rolls their first score or rolls a 7  
      else: 
        continue 				
craps () 	

def main():
  # prompt the user to enter the number of rounds
  num_rounds = int (input ("Enter number of rounds: "))

  # compute the number of times he wins 
  num_wins = 0
  for n in range (num_rounds):
    num_wins +=craps()

  # print the result
  print ("Player wins", num_wins, "out of", num_rounds, "rounds.")

main()
