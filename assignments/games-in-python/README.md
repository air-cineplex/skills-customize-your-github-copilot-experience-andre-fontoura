
# 🎮 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game in Python to practice string manipulation, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Build the Hangman Game

#### Description

Create a command-line Hangman game. The program should choose a hidden word, accept letter guesses from the player, and continue until the player guesses the word or runs out of attempts.

#### Requirements

Completed program should:

- Store at least five words in a predefined list and randomly select one word at the start of each game.
- Accept one letter guess at a time from the player.
- Display the current progress using underscores for unknown letters, such as `_ _ _ _ _`.
- Reveal every occurrence of a correctly guessed letter in the hidden word.
- Track incorrect guesses and display the number of attempts remaining.
- Prevent a repeated guess from being counted as a new attempt.
- End when the player reveals the entire word or uses all available attempts.
- Display a clear win message that includes the guessed word.
- Display a clear lose message that reveals the hidden word.

Example interaction:

```text
Word: _ _ _ _ _
Attempts remaining: 6
Guess a letter: p

Word: p _ _ _ _
Attempts remaining: 6
Guess a letter: z

Incorrect guess. Attempts remaining: 5
```
