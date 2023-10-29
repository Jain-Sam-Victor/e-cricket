import random

def main_menu():
    while True:
        print("Main Menu")
        print("1. Play with computer")
        print("2. Play online")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("You chose to play with the computer.")
            player_choice = input("Choose odd (1) or even (2): ")
            
            if player_choice == '1':
                player_option = 'odd'
                computer_option = 'even'
            elif player_choice == '2':
                player_option = 'even'
                computer_option = 'odd'
            else:
                print("Invalid choice. Please choose 1 for odd or 2 for even.")
                continue

            print(f"You chose {player_option}. Computer has {computer_option}.")

            # Perform the toss
            toss_result = perform_toss()
            if toss_result == player_option:
                print("You won the toss!")
                winner = "player"
            else:
                print("Computer won the toss.")
                winner = "computer"

            # Determine batting or bowling
            if winner == "player":
                batting_choice = input("Choose batting (1) or bowling (2): ")
                if batting_choice == '1':
                    print("You chose batting.")
                    player_score, computer_score = play_game("player")
                elif batting_choice == '2':
                    print("You chose bowling.")
                    player_score, computer_score = play_game("computer")
                else:
                    print("Invalid choice. Please choose 1 for batting or 2 for bowling.")
                    continue
            else:  # Computer's turn to choose
                computer_choice = random.choice(["batting", "bowling"])
                print(f"Computer chose {computer_choice}.")
                if computer_choice == "batting":
                    computer_score, player_score = play_game("computer")
                else:
                    player_score, computer_score = play_game("player")

            print(f"Player's score: {player_score}")
            print(f"Computer's score: {computer_score}")

            

        elif choice == '2':
            print("Online play is not available yet. Check back later.")

        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

def perform_toss():
    toss_result = random.choice(["odd", "even"])
    print(f"The toss result is {toss_result}.")
    return toss_result

def play_game(current_batter):
    player_score = 0
    computer_score = 0
    while True:
        if current_batter == "player":
            player_choice = int(input("Choose a number between 1-10: "))
            computer_choice = random.randint(1, 10)
            print(f"You chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")
            if player_choice == computer_choice:
                player_choice = computer_choice * player_choice
            if abs(player_choice - computer_choice) == 1:
                print("Player is out!")
                print("You scored: ",player_score, "runs" )
                break
            player_score += player_choice
        else:  # Computer's turn to bat
            computer_choice = random.randint(1, 10)
            player_choice = int(input("Choose a number between 1-10: "))
            print(f"You chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")
            if player_choice == computer_choice:
                player_choice = computer_choice * player_choice
            if abs(player_choice - computer_choice) == 1:
                print("Computer is out!")
                print("Computer scored: ",computer_score, "runs" )
                break
            computer_score += computer_choice

    # Get target score    
    if computer_score > player_score:
        target_score = computer_score + 1
    else:
        target_score = player_score + 1

    target = target_score
    print("The target is: ",target, "runs")

    # Second batsman
    while True:
        if current_batter == "player":
            computer_choice = random.randint(1, 10)
            player_choice = int(input("Choose a number between 1-10: "))
            print(f"You chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")
            if player_choice == computer_choice:
                player_choice = computer_choice * player_choice
            if abs(player_choice - computer_choice) == 1:
                print("Computer is out!")
                print("Computer scored: ",computer_score, "runs" )
                break
            computer_score += computer_choice
            # Here is the problem 
            if computer_score > player_score:
                print("Better luck next time. Computer has won the match by", computer_score - player_score, "runs")
                break
        else:
            player_choice = int(input("Choose a number between 1-10: "))
            computer_choice = random.randint(1, 10)
            print(f"You chose: {player_choice}")
            print(f"Computer chose: {computer_choice}")
            if player_choice == computer_choice:
                player_choice = computer_choice * player_choice
            if abs(player_choice - computer_choice) == 1:
                print("Player is out!")
                print("You scored: ",player_score, "runs" )
                break
            player_score += player_choice
            # And here is the problem
            if player_score > computer_score:
                print("Congratulations! You won the match by", player_score - computer_score, "runs")
                break


if __name__ == "__main__":
    main_menu()



