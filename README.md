Mini Scrabble (Python)

A command-line Scrabble-style word game built in Python.

This project simulates a simplified version of Scrabble, where the player places words on a grid using randomly generated letters.

Features

Text-based game board rendered in the terminal
Random letter generation (Scrabble-style tile system)
Word placement with coordinates and direction
Input validation (format, placement rules, available letters)
Dictionary check using a word list
Basic scoring system

How it works

The game displays a grid with a predefined starting word
The player receives 7 random letters

The player inputs moves in the format:

COLUMN:ROW:WORD,DIRECTION
Example: A:1:HELLO,RIGHT

The program validates:
If the word exists in the dictionary
If the placement is valid on the board
If the player has the required letters
If valid:
The word is placed on the board
The player earns a point
New letters are generated

Tech & Concepts

Python
Functions and modular structure
Lists and data handling
Input parsing (regex)
File handling (dictionary lookup)
Basic game logic and state management

Project Structure

main.py – game loop and core logic
data.py – grid and letter data
dict.txt – word list used for validation

Status

Work in progress.

Current limitations:

No advanced scoring (Scrabble rules not fully implemented)
Limited validation for complex board interactions
Letter pool is not reset when empty

What I learned

Structuring a larger program using functions
Breaking down game logic into smaller components
Handling user input and validation
Debugging and iterative development

How to run

Make sure you have Python installed
Install dependency:
pip install tabulate
Run the program:
python main.py

Notes

This project was developed as a learning exercise to practice Python and problem-solving through building a small game.
