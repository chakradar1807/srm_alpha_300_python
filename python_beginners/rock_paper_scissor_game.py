import random

def greeting():
    return "Hi"
response = greeting()
print(response)

def get_choices():
    player_choices = input("enter a choice(rock,paper,scissors: )")
    options = ["rock","paper","scissor"]
    computer_choices = random.choices(options)
    choices = {"player": player_choices,"computer": computer_choices}
    return choices


# choices = get_choices()
# print(choices)
 

def check_win(player,computer):
    print(f"you chose  {player} ,computer chose {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock" and computer == "scissors":
        return "Rock smashes scissors! you win!"
    elif player == "rock" and computer == "paper":
        return "paper covers rock! you lose."
    elif player == "paper" and computer == "scissors":
        return "scissors cuts papers! you lose."
    elif player == "scissors" and computer == "paper":
        return "scissors cuts paper! you win."
    elif player == "scissors" and computer == "rock":
        return "rock hits scissors! you win."
    else:
    #elif player == "paper" and computer == "rock":
        return "paper covers rock! you win."
    

choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)





# if age >= 18:
#     print("you are ")


# food = ["pizza","carrots","eggs"]
# dinner = random.choice(food)


