import random

from project_beginner.guessing_game import guessing_game, computer_guessing_game

if __name__ == '__main__':
    play = random.choice([guessing_game.guess(10), computer_guessing_game.computer_guess(21)])
