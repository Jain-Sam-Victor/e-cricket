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











'''Write a program to print the main menu for the game with options: "Play with computer" and "Play online" but if the "Play online" option is chosen show that the option is not available yet.
When play with computer is chosen then give the player the option to chose from odd or even 
No, the player will choose an option from odd or even then the computer will get the opposite and a random result will be given out 
Now, give the winner the option to choose between batting or bowling, if the winner is player give the choice but if the winner is computer take a random choice
Now give the player an option to choose from any number between 1-10 (1 and 10 included) and also choose random numbers from the computer's side from 1 to 10 simultaneously and only print player's choice first and when the player's choice is printed print the computer's choice. If the computer is batting then the number computer chooses at every chance will get added to its score until it is out and if player is batting, the numbers player choose will get added to the player's score at every chance. The batsman can be out only if coincidentally the number which was chosen by the bowler is adjacent to what the batsman chose (for example - if batsman chose 4 and bowler chose 5 or 3 then the batsman will be out) and when the batsman is out the total score will be printed permanentaly on every ball until the match is over. When the batsman is out the bowler will not bat and if the new batsman makes more runs than the initial batsman (the printed score) the later batsman wins else the intial batsman wins.



Make a game:-
1. Make a main menu with 3 options - "1. Play with computer(When the option is chosen the following steps will take place from 2 point onwards), 2. Play online(when this option is chosen display a message saying that the feature isnt available right now), 3. Quit (quit the game).

Instructions when player chose 1st option i.e. Play with computer
2. Let player choose between odd or even and print the input
3. Now let computer choose a random number from 1 to 10 and also let player choose the number from 1 to 10, then display the player's number first and then computer's number in the output and then add both numbers and check if it forms an odd or an even number if the number is odd then the one who chose odd wins and if the number is even then the one who chose even wins 
4. The winner of the previous function will get to choose from batting or bowling (incase of computer as winner choose random)
5. If the computer is batting then start the match by inputing numbers from 1 to 10 from both players while displaying the numbers they chose(first display player's number). Whoever is batting will get their choices added in their score until they are out and when they are out the batting of other player (who was bowler before) will start and if they cross the score of previous batter by even 1 then the second batter wins the match and if they get out before chasing the score they will lose and the first one will win

Mechanisms:-
1. Both the players will choose numbers from 1 to 10 (computer will choose a random number from 1 to 10 through import random) and whatever the batsman choose gets added to their score
2. The out mechanism: the batsman can be outed only if the number of the bowler is adjacent to the number 
Example - if batsman chose 4 and bowler chose 3, the batsman is out and if the bowler even chose 2, the batsman is still out
3. If both the player's numbers are same/equal then the square of the number will be added to the batsman's score'''