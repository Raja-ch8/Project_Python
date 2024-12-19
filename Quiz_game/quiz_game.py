import random
import emoji

while True :
    question1 = input(f"\n What is the capital of France?\n" "\n 1 ) Paris" "\n 2 ) Rome" "\n 3 ) Madrid")
    choise_user = input(f"\n What is your choise : (1 2 3)\n")
    
    if choise_user == "1" :
        print(f"\nThe correct answer is Paris\n")
        print(emoji.emojize("Good Job! :trophy:", language='alias'))
    
    else:
        print(f"\nWrong answer!\n")
        print(emoji.emojize("Oh no! :thumbs_down::", language='alias'))
        
    question2 = input(f"\n What is the chemical symbol for water?\n" "\n 1 ) CO2" "\n 2 ) H2O" "\n 3 ) O2")
    choise_user = input(f"\n What is your choise : (1 2 3)\n")
    
    if choise_user == "2" :
        print(f"\nThe correct answer is H2O\n")
        print(emoji.emojize("Good Job! :trophy:", language='alias'))
    
    else:
        print(f"\nWrong answer!\n")
        print(emoji.emojize("Oh no! :thumbs_down::", language='alias'))
    
    question3 = input(f"\n Who was the first President of the United States?\n" "\n 1 ) Thomas Jefferson" "\n 2 ) Abraham Lincoln" "\n 3 ) George Washington")
    choise_user = input(f"\n What is your choise : (1 2 3)\n")
    
    if choise_user == "3" :
        print(f"\nThe correct answer is George Washington\n")
        print(emoji.emojize("Good Job! :trophy:", language='alias'))
    
    else:
        print(f"\nWrong answer!\n")
        print(emoji.emojize("Oh no! :thumbs_down:", language='alias'))
        
    question4 = input(f"\n What is the main ingredient in guacamole?\n" "\n 1 ) Tomate" "\n 2 ) Avocado" "\n 3 ) Potato")
    choise_user = input(f"\n What is your choise : (1 2 3)\n")
    
    if choise_user == "2" :
        print(f"\nThe correct answer is Avocado\n")
        print(emoji.emojize("Good Job! :trophy:", language='alias'))
    
    else:
        print(f"\nWrong answer!\n")
        print(emoji.emojize("Oh no! :thumbs_down::", language='alias'))
    
    question5 = input(f"\n Who is the founder of Microsoft?\n" "\n 1 ) Bill Gates" "\n 2 ) Mark Zuckerberg" "\n 3 ) Steve Jobs")
    choise_user = input(f"\n What is your choise : (1 2 3)\n")
    
    if choise_user == "1" :
        print(f"\nThe correct answer is Bill Gates\n")
        print(emoji.emojize("Good Job! :trophy:", language='alias'))
    
    else:
        print(f"\nWrong answer!\n")
        print(emoji.emojize("Oh no! :thumbs_down::", language='alias'))
    
    question6 = input(f"\n How many players are there on a soccer team?\n" "\n 1 ) Nine" "\n 2 ) Eleven" "\n 3 ) Thirteen")
    choise_user = input(f"\n What is your choise : (1 2 3)\n")
    
    if choise_user == "2" :
        print(f"\nThe correct answer is eleven\n")
        print(emoji.emojize("Good Job! :trophy:", language='alias'))
    
    else:
        print(f"\nWrong answer!\n")
        print(emoji.emojize("Oh no! :thumbs_down::", language='alias'))
    
    question7 = input(f"\n Which band released the album Abbey Road?\n" "\n 1 ) The Beatles" "\n 2 ) Led Zeppelin" "\n 3 ) The Rolling Stones")
    choise_user = input(f"\n What is your choise : (1 2 3)\n")
    
    if choise_user == "1" :
        print(f"\nThe correct answer is The Beatles \n")
        print(emoji.emojize("Good Job! :trophy:", language='alias'))
    
    else:
        print(f"\nWrong answer!\n")
        print(emoji.emojize("Oh no! :thumbs_down::", language='alias'))
    
    
    
    play_again = input("Do you want to play again? (y / n): ")
    if play_again.lower() == "y":
        print("Let's play again!")
        continue
    
    elif play_again.lower() == "n":
        print(emoji.emojize("Thank you for playing! Goodbye :wave:", language='alias'))
        break
 

        

   