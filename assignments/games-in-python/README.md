# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a fully playable Hangman game in Python that uses strings, loops, conditionals, and user input to let players guess a hidden word.

## 📝 Tasks

### 🛠️ Word Selection and Game Setup

#### Description

Create the game setup to choose a random word from a predefined list and initialize the puzzle state for the player.

#### Requirements
Completed program should:

- Define a list of possible words for the game.
- Randomly select one word each time the game starts.
- Initialize a hidden word display with underscores for each letter.
- Track letters guessed and remaining attempts.

### 🛠️ Letter Guessing and Game Loop

#### Description

Implement the main game loop to process letter guesses, update the display, and end the game when the player wins or loses.

#### Requirements
Completed program should:

- Prompt the player to guess one letter at a time.
- Reveal correctly guessed letters in the hidden word display.
- Count incorrect guesses and reduce remaining attempts accordingly.
- End the game with a win message when the word is fully guessed.
- End the game with a lose message when attempts run out.

### 🛠️ User Feedback and Results

#### Description

Display the current game state and final result clearly, so the player always knows their progress.

#### Requirements
Completed program should:

- Show the current progress of the word after each guess, e.g. `h _ n g m a n`.
- Show the number of incorrect guesses remaining.
- Inform the player when a guessed letter was incorrect or already guessed.
- Print a final message declaring whether the player won or lost.

