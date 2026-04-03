from tabulate import tabulate
from data import grid_list, scrabble_list
import random
import sys
import re
import os

def main():
# Prints initial grid with hard-coded word HOUSE.
    tab_grid = tabulate(grid_list, headers="firstrow", tablefmt="double_grid")
    print(tab_grid)

    # Prints seven random letters
    letters = letters_generator()
    points = 0
    
    while True:
        if points < 3:
            print(f"Your random letters are: \033[93m{' '.join(letters)}\033[0m")
            print("Use following format for your input: COLUMN:ROW:LETTERS,DIRECTION\nExample: A:1:DAN,RIGHT\n" \
            "The input is case-insensitive.\nDirection can be only 'RIGHT' or 'DOWN'\nType 'exit' to quit the game." )

            user_input = input("Enter coordinates and direction: ").upper()
            if user_input == "EXIT":
                sys.exit("Thank you for playing.")

            clear_screen()

            coordinates = convert_coordinates(user_input)

            success = play_turn(coordinates, letters)

            if success == "invalid_word":
                tab_grid = tabulate(grid_list, headers="firstrow", tablefmt="double_grid")
                print(tab_grid)
                print("\033[91mNot a valid word.\033[0m")
            elif success is False:
                tab_grid = tabulate(grid_list, headers="firstrow", tablefmt="double_grid")
                print(tab_grid)
                print("\033[91mInvalid move. Try again.\033[0m")

            elif success:
                points = points + 1
                letters = letters_generator()
                print(tabulate(grid_list, headers="firstrow", tablefmt="double_grid"))
                print("\033[92mGreat move! You've got new letters!\033[0m")
                print(f"\033[96mYou have {points} points.\033[0m")
        else:
            sys.exit("Congratulations, you've reached 3 points!")


# Checks operating system and decides which command to use to clear screen.
def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

# Dictionary check
def dict_check(coordinates):
    with open("dict.txt", "r") as file:
        for line in file:
            if coordinates[2] == line.strip():
                return True
        return False

# Picks 7 letters from data.py, removes those letters from scrabble_list.
def letters_generator():
    letter_count = 0
    letter_list = []
    while letter_count <= 6:
        letter = random.choice(scrabble_list)
        letter_list.append(letter)
        scrabble_list.remove(letter)
        letter_count = letter_count + 1
    return letter_list

# Splits user input into coordinates, letters and direction.
def convert_coordinates(user_input):
    input_split = re.split(r"[:,]", user_input)

    if input_split[0] in grid_list[0]:
        col_letter = grid_list[0].index(input_split[0])
    row_text = int(input_split[1])
    letter = input_split[2]
    direction = input_split[3]
    return(col_letter, row_text, letter, direction)

# Checks if the user input letters are available in the rack.
# Returns True, indicating that the move is valid.
def rack_check(result, letters):
    letter_list = result
    temp_rack = letters.copy()

    for letter in letter_list:
        if letter in temp_rack:
            temp_rack.remove(letter)
        else:
            return False
    return True

# Checks if the RIGHT move is valid and returns only the letters needed to form a word,
# filtering out letters already on the grid.
def direction_right(coordinates):
    needed_letters = []
    current_col = coordinates[0]
    current_row = coordinates[1]


    if len(coordinates[2]) > 1 and coordinates[3] == "RIGHT":
        for letter in coordinates[2]:
            cell = grid_list[current_row][current_col]
            if cell == "":
               needed_letters.append(letter)
               current_col += 1
               continue
            elif cell == letter: #This is the place to fix the intersections!(maybe)
               current_col += 1
               continue
            else:
                return False
    return needed_letters

# Checks if the DOWN move is valid and returns only the letters needed to form a word,
# filtering out letters already on the grid.
def direction_down(coordinates):
    needed_letters = []
    current_col = coordinates[0]
    current_row = coordinates[1]


    if len(coordinates[2]) > 1 and coordinates[3] == "DOWN":
        for letter in coordinates[2]:
            cell = grid_list[current_row][current_col]
            if cell == "":
               needed_letters.append(letter)
               current_row += 1
               continue
            elif cell == letter: #This is the place to fix the intersections!(maybe)
               current_row += 1
               continue
            else:
                return False
    return needed_letters

# Coordinates the flow of a single turn.
# Checks the dictionary, validates board placement
# Checks the rack and commits the move to the grid.
def play_turn(coordinates, letters):
    if not dict_check(coordinates):
        invalid_word = "invalid_word"
        return invalid_word

    if coordinates[3] == "RIGHT":
        result = direction_right(coordinates)
        if result is False:
            return False
        if not rack_check(result, letters):
            return False
        place_letters(coordinates)
        return True

    if coordinates[3] == "DOWN":
        result = direction_down(coordinates)
        if result is False:
            return False
        if not rack_check(result, letters):
            return False
        place_letters(coordinates)
        return True

    return False


# Places the letters on the grid.
def place_letters(coordinates):
    current_col = coordinates[0]
    current_row = coordinates[1]
    if coordinates[3] == "RIGHT":
        for letter in coordinates[2]:
            cell = grid_list[current_row][current_col]
            if cell == "":
                grid_list[current_row][current_col] = letter
                current_col = current_col + 1
            elif cell == letter:
                current_col += 1
                continue

    if coordinates[3] == "DOWN":
        for letter in coordinates[2]:
            cell = grid_list[current_row][current_col]
            if cell == "":
                grid_list[current_row][current_col] = letter
                current_row = current_row + 1
            elif cell == letter:
                current_row += 1
                continue

    tab_grid = tabulate(grid_list, headers="firstrow", tablefmt="double_grid")

    return tab_grid



main()
