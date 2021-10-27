# Nicholas Handberg, Assignment 2, 1/20/2021
# Topics: Conditional Statements, while loop

SAME_DICE_MULT = 2                                                                                  # Reward multiplier for dice rolling same result.

import random                                                                                       # Imports the random module
player_money = 250                                                                                  # Assigns the intial value of player_money
another_game = 'y'                                                                                  # Assigns the inital value of another_game to trigger the while loop

print("Welcome to the Dice Game.")                                                                  # Prints welcome message to user's display
print("     _______        _______\n    /O     /\      /O     /\ ")                                 # Prints ASCII art of two dice. Credit: Morfina
print("   /   O  /O \    /   O  /O \ \n  /_____O/    \  /_____O/    \  ")
print("  \O    O\    /  \O    O\    / \n   \O    O\ O/    \O    O\ O/ ")
print("    \O____O\/      \O____O\/")
print(f"\nYou are given ${player_money} to start.")                                                 # Prints your starting money and that the game will end when you run out of money
print("You can't play once you run out of money.")
#----------------------------------------------------------------------------------- 
while player_money > 0 and another_game == 'y':                                                     # Starts the while loop that loops as long as the user has money to bet and another_game = 'y'
    player_bet = int(input("\nHow much are you betting?  "))                                        # Gets the ammount of money the user wants to bet 
    while (player_money < player_bet) or (player_bet <= 0):                                         # While loop to check if the bet the user inputed is valid (0 < player_bet <= player_money)
        if player_money < player_bet:                                                               # If the user is betting more money than they have, it will ask them to re-enter the bet
            print("\nYou do not have enough for that bet.")                                         
            player_bet = int(input(f"Please enter an ammount no greater than {player_money}:  "))   
        else:                                                                                       # If the user enters a negative number or 0, it will ask them to re-enter the bet
            print("\nYour bet cannot be negative or zero.")
            player_bet = int(input("Please enter an ammount greater than 0:  ")) 
#-----------------------------------------------------------------------------------            
    player_sum = int(input("\nWhat is the sum of the two dice?  "))                                 # Gets the sum of the dice from the user
    while (player_sum < 2) or (player_sum > 12):                                                    # While loop to check if the user's prediction is within the allowed range die sums
        player_sum = int(input("\nPlease enter a number from 2 to 12:  "))                          # Asks the user to re-enter prediction within the allowed range
    dice_1 = int(random.randrange(1,7))                                                             # Simulates the random dice roll for dice_1
    dice_2 = int(random.randrange(1,7))                                                             # Simulates the random dice roll for dice_2
    dice_sum = dice_1 + dice_2                                                                      # Adds the values of dice_1 and dice_2
    print(f"\nDie 1 is: {dice_1} \nDie 2 is: {dice_2}")                                             # Prints the values of the die to the user's screen
#----------------------------------------------------------------------------------- 
    if player_sum == dice_sum:                                                                      # Checks if the user's predicted sum equals the simulated sum
        if dice_1 == dice_2:                                                                        # Checks if the die are equal in value
            player_money += SAME_DICE_MULT * player_bet                                             # Multiplies the user's bet by the multiplier and adds the value to the user's money
            print(f"\nYou win ${player_bet * SAME_DICE_MULT}")                                      # Prints the ammount of winnings to the user's display
        else:
            player_money += player_bet                                                              # Adds the user's bet to the user's money otherwise
            print(f"\nYou win ${player_bet}")                                                       # Prints the ammount of winnings to the user's display
    else:
        player_money -= player_bet                                                                  # If the predicted sum and simulated sum are not equal, subtracts the user's bet from their money
        print(f"\nYou lost ${player_bet}")                                                          # Prints the ammount lost to the user's display
    print(f"Your current balance is ${player_money}")                                               # Prints the user's current balance after the calculations are complete
#----------------------------------------------------------------------------------- 
    another_game_temp = str(input("\nDo you want to play another game? (Y/N)  "))                   # Asks the user if they want another game and gets an input Y/N from the user to store in a temp variable
    another_game = another_game_temp.lower()                                                        # Assigns the .lower() of the temp variable to the another_game variable so case doesnt matter from user input
    while another_game != "y" and another_game != "n":                                              # While loop to check if the user's input is valid ('y' or 'n')
        another_game_temp = str(input("\nPlease enter either Y or N for your answer:  "))           # Repeats the same code as above until the user input is valid
        another_game = another_game_temp.lower()
#-----------------------------------------------------------------------------------                # Once the user breaks the while loop from either running out of money or responding 'n' to another game, runs the following
if another_game == 'n':                                                                             # Checks if the user inputed 'n' for another_game and prints "Thanks for playing!"      
    print("\nThanks for playing!")   
elif player_money <= 0:                                                                             # Checks if the user ran out of money and prints "You have ran out of money, Thanks for playing!"
    print("\nYou have ran out of money, Thanks for playing!")