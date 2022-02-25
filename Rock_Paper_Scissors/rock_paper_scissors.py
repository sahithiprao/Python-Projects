import random

while True:
    
    user_action = input("Please enter your choice (Rock, Paper, Scissors): ")
    actions = ["Rock","Paper", "Scissors"]
    computer_choice = random.choice(actions)

    print(f"User choice is  {user_action} and computer_choice is {computer_choice}")

    #conditions
    if(user_action == computer_choice):
        print("HUH! Both are tie")
    elif (user_action == "Rock"):
        if (computer_choice == "Scissors"):
            print("yayy! Rock Beats Scissors and User won")
        else:
            print('Paper Covers Rock! Computer won')
    elif (user_action == "Paper"):
        if (computer_choice == "Rock"):
            print("yayy! Paper Covers Rock and User won")
        else:
            print('Scissors Cut Paper Computer won')
    elif (user_action == "Scissors"):
        if (computer_choice == "Paper"):
            print("yayy! Scissors Cut Paper and User won")
        else:
            print('Rock Beats Scissors Computer won')

    play_again = input("Do you wanna play again? y/n: ")
    if play_again.lower() != "y":
        break