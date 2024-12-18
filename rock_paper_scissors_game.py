import random 
import emoji

while True:

    user_action = input(f"\n Welcome \U0001F600 to the Rock, Paper, Scissors game!\n Enter a choise (rock, paper, scissors): ")

    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print(f"\n User choise {user_action} , Computer choise {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action} . It's a tie ") 
        print("\U0001F600") 

    elif user_action == "paper":
        if computer_action == "scissors": 
            print("Scissors cuts paper! ")
            print(emoji.emojize(" YOU LOSE :thumbs_down:"))

    elif user_action == "scissors":
        if computer_action == "paper": 
            print("Scissors cuts paper! ")
            print(emoji.emojize(" YOU WIN :trophy:"))

    elif user_action == "rock":
        if computer_action == "scissors": 
            print("Rock smashes scissors")
            print(emoji.emojize(" YOU WIN :trophy:"))

    elif user_action == "scissors":
        if computer_action == "rock": 
            print("Rock smashes scissors! ")
            print(emoji.emojize(" YOU LOSE :thumbs_down:"))


    elif user_action == "rock":
        if computer_action == "paper": 
            print("Paper covers rock! ")
            print(emoji.emojize(" YOU LOSE :thumbs_down:"))
        

    elif user_action == "paper":
        if computer_action == "rock": 
            print("Paper covers rock! ")
            print(emoji.emojize(" YOU WIN :trophy:"))
            
    play_again = input("Do you want to play again? (y / n): ")
    if play_again.lower() == "y":
        print("Let's play again!")
        continue
    
    elif play_again.lower() == "n":
        print(emoji.emojize("Goodbye :wave:", language='alias'))
        break
 
   
    