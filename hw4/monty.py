# Vincent O'Leary
# Assignment 4 for CS 171-064
# Monty Hall Analysis

# Import the random library and set the seed for testing purposes
import random
random.seed()

# Define the functions for analysis
def setupDoors():
    # Create the baseline list of doors
    whats_behind_door = ['G','G','G']
    # Pick the winning door
    lucky_door = random.randint(1,3)
    # Remove the goat and add the car behind the lucky door number
    whats_behind_door.insert(lucky_door-1, 'C')
    whats_behind_door.pop(lucky_door)
    return whats_behind_door

def playerDoor():
    # Choose a door for the player
    player_choice = random.randint(1,3)
    return player_choice

def montyDoor(Doors, Player):
    # Create another baseline list of doors
    all_knowing_monty = ['G','G','G']
    # Remove the goat and add the car behind the lucky door from setupDoors()
    all_knowing_monty[Doors-1]='C'
    # If the player chooses wining door, Monty picks the first goat door
    if Doors == Player:
        monty_choice = all_knowing_monty.index('G')+1
    # If the player choose a losing door, Monty picks the remaining goat door
    else:
        all_knowing_monty[Player-1]='P'
        monty_choice = all_knowing_monty.index('G')+1
    return monty_choice

def playRound():
    # Play Let's Make a Deal
    # Run all three functions, save the door number for the car and the player's choice
    foo = setupDoors()
    door_car = foo.index('C')+1
    door_choice= playerDoor()
    montyDoor(door_car,door_choice)
    # If player chooses winning door, they will win if they stay = 0
    if door_car == door_choice:
        outcome = 0
    # If player chooses a losing door, they will win if they switch = 1
    else:
        outcome = 1
    return outcome

# Print welcome statement and instructions
print('Welcome to the Monty Hall Analysis')
print('Enter \'exit\' to quit')

# Run the main function
if __name__=='__main__':
    num_tests = input('How many tests should we run?\n')
    # Run the program until the user enters 'exit'
    while num_tests != 'exit':
        # If the input is not a number, ask again without crashing
        try:
            i = 1
            outcome_lis = []
            # Play the number of rounds specified
            while i <= int(num_tests):
                baz = playRound()
                outcome_lis.append(baz)
                i = i + 1
            # Switch wins if the outcome is 1, sum of all outcomes is the number of switch wins
            total_wins = sum(outcome_lis)
            switch_wins = 100 * float((float(total_wins)) / float(num_tests))
            stay_wins = float((100 - switch_wins))
            # Print the results of the games
            print('Stay won %.1f%% of the time.' % stay_wins)
            print('Switch won %.1f%% of the time.' % switch_wins)
        except ValueError as e:
            print('I didn\'t like that. Please enter a number!')
        # Continue to ask the user for a value to make a new prediction
        num_tests = (input('How many tests should we run?\n'))
    print('Done already?\nGoodbye! Come back again soon.')
