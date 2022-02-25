import random
from enum import IntEnum
# allows to create attributes and assign values similar to invidual assignment

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

#returns user action 
def get_user_selection():
    #this helps when new actions needs to be added
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choice_str = ",".join(choices)
    selection = int(input(f"Enter a choice ({choice_str}): "))
    action = Action(selection)
    return action

#computer selection
def get_computer_selection():
    selection = random.randint(0, len(Action) - 1) 
    print(selection)
    #randon.randint returns a random value between a specified min and max inclusive
    action = Action(selection)
    return action

def winner_selection(user_action, computer_choice):
    if(user_action == computer_choice):
        print("HUH! Both are tie")
    elif (user_action == Action.Rock):
        if (computer_choice == Action.Scissors):
            print("yayy! Rock Beats Scissors and User won")
        else:
            print('Paper Covers Rock! Computer won')
    elif (user_action == Action.Paper):
        if (computer_choice == Action.Rock):
            print("yayy! Paper Covers Rock and User won")
        else:
            print('Scissors Cut Paper Computer won')
    elif (user_action == Action.Scissors):
        if (computer_choice == Action.Paper):
            print("yayy! Scissors Cut Paper and User won")
        else:
            print('Rock Beats Scissors Computer won')

while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str =  f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_choice = get_computer_selection()
    winner_selection(user_action, computer_choice)

    play_again = input("Play Again? (y/n) ")
    if play_again.lower() != "y":
        break
