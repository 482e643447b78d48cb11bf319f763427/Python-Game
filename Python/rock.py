import random

def com_choice():
    random_number = random.randint(1, 3)
    option = {1: 'Rock', 2: 'Scissor', 3: 'Paper'}
    computer_choice = option[random_number]
    return computer_choice

#result = com_choice()
#print(result)

def user_choice():
    user_ch = input("Enter Rock / Paper / scissor")
    return user_ch

#result = user_choice()
#print(result)

def final_result(user, computer):
    if user == computer:
        return "Draw"

    elif (user == "Paper" and computer == "Rock"):
        return "Win"

    elif (user == "Rock" and computer == "Scissor"):
        return "Win"
    
    elif (user == "Scissor" and computer == "Paper"):
        return "Win"
    
    else:
        return "Lose"
    
user = user_choice()
computer = com_choice()
result = final_result(user, computer)

print(f"Player:{user}")
print(f"Computer:{computer}")
print(f"Final Result: {result}")