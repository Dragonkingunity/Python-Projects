import random
print("Welcome to Rock Paper Scissors")
#Starting choice
pick = ("Rock", "Paper", "Scissors")
#Allows game to keep going
playing = True

#For conditions for power ups
win = "You Win!!! :) :)"
lose = "You Lose!!! :( :("
tie = "Tied so sad. :("
outcome = tie

#Looping the game
while playing:

#Reseting the player and Ai choice
    player = None
    ai = random.choice(pick)

    #Reward if win
    if outcome == win:

        #Letting player see Ai choice before they choose
        print("AI: ", ai)

        #Playing again
        while player not in pick:
            player = input("Choose (Rock, Paper, Scissors)")

        print("Player: ", player)

        if player == ai:
            outcome = tie
            print(outcome)

        elif player == "Paper" and ai == "Rock":
            outcome = win
            print(outcome)

        elif player == "Rock" and ai == "Scissors":
            outcome = win
            print(outcome)

        elif player == "Scissors" and ai == "Paper":
            outcome = win
            print(outcome)

        else:
            outcome = lose
            print(outcome)
    
    elif outcome == tie:

    #Not allowing the player to type anything else
        while player not in pick:
            player = input("Choose (Rock, Paper, Scissors)")

        # Printing player and Ai choices
        print("AI: ", ai)
        print("Player: ", player)

        # Decides what happens win lose or tie
        if player == ai:
            outcome = tie
            print(outcome)

        elif player == "Paper" and ai == "Rock":
            outcome = win
            print(outcome)

        elif player == "Rock" and ai == "Scissors":
            outcome = win
            print(outcome)

        elif player == "Scissors" and ai == "Paper":
            outcome = win
            print(outcome)

        else:
            outcome = lose
            print(outcome)




    #Allows player to exit game
    if not input("Play again? (y/n): ").lower() == "y":
        playing = False

print("Hope you enjoyed!!")
