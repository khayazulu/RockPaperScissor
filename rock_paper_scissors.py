#Author: Sandile Khayelihle Zulu

import random

#Function to print welcome message and rules 
def rules(name):
	print("")
	print("-WELCOME,", name.upper(),"!!! to Rock Paper, Scissors, a game of chance")
	print("outsmart the other.")
	print("=========================")
	print("___The rules are as follows___")
	print("=========================")
	print("-This game is Human VS Computer.")
	print("-A random choice will be generated for computer choice in each round")
	print("-You will be prompted to choose a weapon between Rock, Paper or Scissors")
	print("-Paper wraps rock, Rock smashes Scissors and Scissors cuts Paper ")
	print("-You wil be credited 3 points for a win,1 point for a draw and 0 for a lose" )
	print("-After all rounds you will be given the overall results")
	print("-")
	print("\n","__________GOOD LUCK!!!__________")
	print("")

def choice(): 
	print("____________________________________________")
	print("Menu")
	print("1. Rock\n2. Paper\n3. Scissors\nq. Quit ") 
	print("____________________________________________")
	player = input("Your Choice >> ")
	return player

 #Check who wins for each round and returns computer, player or a draw
def roundResult(computer, player, round, player_name):

	if (computer == player):
		print("Round", round, "is a draw")
		results = "draw"
	elif(computer == 1 and player == 3):
		print("Computer wins round", round)
		results = "computer"
	elif(computer == 2 and player == 1):
		print("Computer wins round", round)
		results = "computer"
	elif(computer == 3 and player == 2 ):
		print("Computer wins round", round)
		results = "computer"
	else:
		print(player_name,"wins round", round)
		results = "player"
		
	return results
		
#Assign initial variables
player_score = 0 
computer_score = 0
round = 0

player_name = input ("Enter Your name here: ")
rules(player_name)

player_choice = choice()

while(player_choice  != 'q'):
        round += 1
        computer_choice = random.randint(1,3)
        player = int(player_choice)
        print("Computer selected",computer_choice)
        print("")
        print("You selected",player_choice)
        print("")
        
        round_winner = roundResult(computer_choice, player, round, player_name)
        
        if (round_winner == "draw"):
              player_score +=  1
              computer_score += 1
       
        elif(round_winner == "computer"):
              computer_score += 3
              
        else:
              player_score += 3
	
        player_choice = choice()
	    
#Check overall score and print results   

print ("")
print ("Your overall score is,", player_score, "out of",((round)*3),"points")
print ("computer score is, ", computer_score, "out of",((round)*3),"points")    
print ("")
    
if player_score == computer_score:
    print ("Draw")

elif player_score > computer_score:
    print ("____Congratulations!!",player_name,"YOU WON")

elif player_score < computer_score:
    
    print ("You lost, Better luck next time ")
   
print (".....Thank You",player_name,"for playing....!!")
print ("")
print ("_____Brought to you by Khaya Zulu_____")