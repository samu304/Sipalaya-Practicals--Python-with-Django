# Rock Paper Scissor game in python

import random
choices = ["R","P","S"]

def user_choice():
    while True:
        choice = input("Enter your choice: ").upper()
        if choice in choices:
            return choice
        else:
            print("Invalid choice. Please try again")

def computer_choice():
    return random.choice(choices)

def winner(user, computer):
    if user == computer:
        return "It's a tie"
    elif (user == "R" and computer == "S") or (user == "S" and computer == "P") or (user == "P" and computer == "R"):
        return "User Wins"
    else:
        return "Computer Wins"
    
def play_game():
    print("********************************************")
    print("Welcome to the Rock, Paper and Scissor Game")
    print("********************************************")
    
    while True:
        user_wins = 0
        computer_wins = 0
        for i in range(1,4):
            
            print(f"\nRound {i} ")
            player = user_choice()
            comp = computer_choice()

            print("User chose:", player)
            print("Computer chose:", comp)

            result = winner(player, comp)
            print(result)

            if result == "User Wins":
                user_wins += 1
            elif result == "Computer Wins":
                computer_wins += 1

        print("\nRound 3 ends here........")
        print("Final Results:\n")

        print(f"User won {user_wins} times")
        print(f"Computer won {computer_wins} times")

        if user_wins > computer_wins:
            print("Congratulations! User Won\n")
        elif computer_wins > user_wins:
            print("You lost, better luck next time\n")
        else:
            print("You both played great. But it's a tie\n")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

play_game()